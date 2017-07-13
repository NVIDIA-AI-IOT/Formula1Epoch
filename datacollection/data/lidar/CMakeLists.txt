cmake_minimum_required(VERSION 2.8.11)

if(${CMAKE_SYSTEM_NAME} MATCHES "Linux")
  set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=c99 -Wall -Wextra -pedantic")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wall -Wextra -pedantic")
elseif(${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
  set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=c99 -Wall -Wextra -pedantic")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wall -Wextra -pedantic")
elseif(${CMAKE_SYSTEM_NAME} MATCHES "Windows")
  # Turn on the ability to create folders to organize projects (.vcproj)
  # It creates "CMakePredefinedTargets" folder by default and adds CMake
  # defined projects like INSTALL.vcproj and ZERO_CHECK.vcproj
  set_property(GLOBAL PROPERTY USE_FOLDERS ON)
else()
  message(FATAL_ERROR "System not yet supported. Please open a ticket.")
endif()

find_package(Threads REQUIRED)
find_package(Sweep REQUIRED)

add_executable(lidar_data_retrieval main.cpp)
target_link_libraries(lidar_data_retrieval PRIVATE ${LIBSWEEP_LIBRARY} ${CMAKE_THREAD_LIBS_INIT})
target_include_directories(lidar_data_retrieval SYSTEM PRIVATE ${LIBSWEEP_INCLUDE_DIR})

