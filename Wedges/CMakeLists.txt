cmake_minimum_required(VERSION 2.8)
project(wedges)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_COMPILER g++)
set(CMAKE_VERBOSE_MAKEFILE ON)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} --std=c++11")

# for optimze
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Ofast")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fopenmp")

include_directories(include)
file(GLOB SOURCE_FILES src/*.C)
link_directories(/group/dpa/local/openvdb/lib)
add_executable(wedges ${SOURCE_FILES} src/wedges.C include/WedgeFunc.h include/Particle.h)
target_link_libraries(wedges Half tbb openvdb OpenImageIO)
target_include_directories(wedges PUBLIC /group/dpa/local/openvdb/include)