#include <chrono>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <signal.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/time.h>
#include <unistd.h>

#include <sweep/sweep.hpp>

using namespace std;
using namespace sweep;

void ctrc_exit(int signal) {
    printf("Exiting from signal: %d \n", signal);
    exit(1);
}

int main(int argc, char* argv[]) try {
    struct timeval tv;  // struct for calculating timestamp
    struct sigaction handler; // Creates handler

    // Handler properties
    handler.sa_handler = ctrc_exit;
    sigemptyset(&handler.sa_mask);
    handler.sa_flags = 0;

    // Run the listener
    sigaction(SIGINT, &handler, NULL);

    // Checking USB device port   
    if (argc != 2) {
        cerr << "Usage: lidar device\n";
        return EXIT_FAILURE;
    }

    cout << "Constructing sweep device..." << endl;
    sweep::sweep device{argv[1]};

    device.set_sample_rate(1000);

    cout << "Motor Speed Setting: " << device.get_motor_speed() << " Hz" << endl;
    cout << "Sample Rate Setting: " << device.get_sample_rate() << " Hz" << endl;

    cout << "Beginning data acquisition as soon as motor speed stabilizes..." << endl;
    device.start_scanning();

    // Set up variables for timestamp
    unsigned long long millisec;
    ofstream textFile;

    while(true) {
        // Receiving scan
        const scan scan = device.get_scan();

        for (const sample& sample : scan.samples) {
            // Getting timestamp value
            gettimeofday(&tv, NULL);
            millisec = (unsigned long long)(tv.tv_sec) * 1000 + (unsigned long long)(tv.tv_usec) / 1000;

            // Printing scan values
            cout << "angle " << sample.angle << " distance " << sample.distance << " strength " << sample.signal_strength << " timestamp " << millisec << "\n";

            // Putting data to a text file
            textFile.open ("scandata.txt", ios_base::app);
            textFile << "angle " << sample.angle << " distance " << sample.distance << " strength " << sample.signal_strength << " timestamp " << millisec << "\n";
            textFile.close();
        }
    }

    device.stop_scanning();
} catch (const device_error& e) {
    cerr << "Error: " << e.what() << endl;
}
