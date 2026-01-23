cmake_minimum_required(VERSION 3.8)
project(hector_imu_tools)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)

include_directories(include)

add_executable(imu_filter_node
  src/imu_filter.cpp
)

ament_target_dependencies(imu_filter_node
  rclcpp
  sensor_msgs
  geometry_msgs
)

install(TARGETS
  imu_filter_node
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
