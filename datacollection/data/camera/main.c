#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>

#include <string.h>
#include <assert.h>
#include <math.h>
#include <time.h>

#include <errno.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/time.h>
#include <sys/mman.h>
#include <sys/ioctl.h>

#include <linux/videodev2.h>

#include <signal.h>

#define CLEAR(x) memset(&(x), 0, sizeof(x))

struct v4l2_capability cap;
struct v4l2_format format;
struct v4l2_requestbuffers bufrequest;
struct v4l2_buffer bufferinfo;
struct v4l2_buffer bufferstreaminfo;
struct timeval tv;

static volatile int exitHandle = 1;

void intHandler(int exitSignal) {
    exitHandle = 0;
}

int main(int argc, char *argv[]) {

    int fd;
    if ((fd = open("/dev/video0", O_RDWR)) < 0) { // make sure to change accordingly
        perror("open");
        exit(1);
    } else {
        printf("Camera opened.\n");
    }

    if(ioctl(fd, VIDIOC_QUERYCAP, &cap) < 0) {
        perror("VIDIOC_QUERYCAP");
        exit(1);
    } else {
        printf("Query worked\n");
    }

    if(!(cap.capabilities & V4L2_CAP_VIDEO_CAPTURE)) {
        fprintf(stderr, "The device does not handle single-planar video capture. \n");
        exit(1);
    } else {
	printf("Passed capabilities\n");
    }
    
    format.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
    format.fmt.pix.pixelformat = V4L2_PIX_FMT_MJPEG;
    format.fmt.pix.width = 800; // arbitrary fix later
    format.fmt.pix.height = 600; // arbitrary fix later

    if(ioctl(fd, VIDIOC_S_FMT, &format) < 0) {
        perror("VIDIOC_S_FMT");
        exit(1);
    } else {
        printf("Format works yay!\n");
    }

    // Allocating buffer memory
    bufrequest.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
    bufrequest.memory = V4L2_MEMORY_MMAP;
    bufrequest.count = 1;

    if(ioctl(fd, VIDIOC_REQBUFS, &bufrequest) < 0) {
        perror("VIDIOC_REQBUFS");
        exit(1);
    } else {
        printf("Requested buffers\n");
    }

    memset(&bufferinfo, 0, sizeof(bufferinfo));
    bufferinfo.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
    bufferinfo.memory = V4L2_MEMORY_MMAP;
    bufferinfo.index = 0;
    
    if(ioctl(fd, VIDIOC_QUERYBUF, &bufferinfo) < 0) {
        perror("VIDIOC_QUERYBUF");
        exit(1);
    } else {
        printf("Cleared structure memory space\n");
    }
    
    void* buffer_start = mmap(
        NULL,
        bufferinfo.length,
        PROT_READ | PROT_WRITE,
        MAP_SHARED,
        fd,
        bufferinfo.m.offset
    );

    if(buffer_start == MAP_FAILED) {
        perror("mmap");
        exit(1);
    } else {
        printf("Buffer allocated\n");
    }

    // Streaming buffer
    memset(&bufferstreaminfo, 0, sizeof(bufferstreaminfo));
    bufferstreaminfo.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
    bufferstreaminfo.memory = V4L2_MEMORY_MMAP;
    bufferstreaminfo.index = 0;

    // Activate streaming
    int type = bufferstreaminfo.type;
    if(ioctl(fd, VIDIOC_STREAMON, &type) < 0){
       perror("VIDIOC_STREAMON");
       exit(1);
    }

    // Set up to get timestamp
    gettimeofday(&tv, NULL);
    unsigned long long millisec = (unsigned long long)(tv.tv_sec) * 1000 + (unsigned long long)(tv.tv_usec) / 1000;

    // Set up for image file name
    int jpegfile;

    char* imagepath = "/images/";
    char* imagejpeg = ".jpeg";
    char* imagenum;
    char* fullimagepath;

    // Set up for image number from text file
    int count;
    FILE *countfile;
    char scount[10];

    // Set "timestampfile" to type file
    FILE *timestampfile;
    char* timestampnum;

    unsigned long long lastseconds;

    // Set up for timing to make it 3 fps
    unsigned long long start_t = millisec;
    unsigned long long end_t = millisec;
    unsigned long long total_t;
    
    signal(SIGINT, intHandler);

    while (exitHandle) { // no longer stupid
       if(ioctl(fd, VIDIOC_QBUF, &bufferstreaminfo) < 0) {
	    perror("VIDIOC_QBUF");
            exit(1);
        } else {
//        printf("Put the buffer in incoming queue\n");
        }

        if(ioctl(fd, VIDIOC_DQBUF, &bufferstreaminfo) < 0) {
            perror("VIDIOC_QBUF");
            exit(1);
        } else {
//	    printf("Buffer waited\n");
        }

  	// Getting timestamp in milliseconds and printing it
        gettimeofday(&tv, NULL);
	millisec = (unsigned long long)(tv.tv_sec) * 1000 + (unsigned long long)(tv.tv_usec) / 1000;

	// Getting time to compensate frames per second
	end_t = millisec;
	total_t = end_t - start_t;
	printf("Total time: %llu \n", total_t);

	// Get 3 frames every second
 	if (total_t > (unsigned long long)(1.0 / 3.0 * 1000)) {
	    start_t = millisec;
	    // Print the image timestamp to console
  	    printf("Timestamp: %llu", millisec);
	    // Write the timestamp to "timestamp.txt"
            timestampnum = malloc(16);
            snprintf(timestampnum, 16, "%llu\n", millisec);

	    timestampfile = fopen("timestamp.txt", "a");
	    fprintf(timestampfile, "%llu\n", millisec);
	    fclose(timestampfile);

  	    // getting image number from file
	    countfile = fopen("count.txt", "r");
            fscanf(countfile, "%s", scount);
	    sscanf(scount, "%d", &count);
	    fclose(countfile);

	    // setting number for next image
	    countfile = fopen("count.txt", "w");
	    fprintf(countfile, "%d", count + 1);
	    fclose(countfile);

	    // getting full image path from coverting integer to char* and combine them, maybe change this to be less stupid?
            imagenum = malloc(16);
            snprintf(imagenum, 16, "%d", count);
         
	    fullimagepath = malloc(strlen(imagepath) + strlen(imagenum) + strlen(imagejpeg));
            strcpy(fullimagepath, imagepath);
            strcat(fullimagepath, imagenum);
            strcat(fullimagepath, imagejpeg);
 //        printf("%s \n", fullimagepath);

            // writing to image
            if((jpegfile = open(fullimagepath, O_WRONLY | O_CREAT, 0660)) < 0){
                 perror("open");
                 exit(1);
            } else {
//     	         printf("Opened image\n");
            }

            write(jpegfile, buffer_start, bufferstreaminfo.length);
            close(jpegfile);
            free(fullimagepath);
	}	

	lastseconds = tv.tv_sec;
	printf("Seconds: %llu \n", lastseconds);

     }

     // Deactivate streaming
     if(ioctl(fd, VIDIOC_STREAMOFF, &type) < 0) {
 	 perror("VIDIOC_STREAMOFF");
	 exit(1);
     }
     // Writing as jpeg
     close(fd);

        
    return EXIT_SUCCESS;
}
