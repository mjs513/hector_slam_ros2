cmake_minimum_required(VERSION 3.8)
project(hector_lightweight_map_transport)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)

# Install Python nodes
install(
  PROGRAMS
    scripts/map_compressor
    scripts/map_decompressor
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
