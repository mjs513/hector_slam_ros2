cmake_minimum_required(VERSION 3.8)
project(hector_imu_tools)

# Dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)

# Executable
add_executable(pose_and_orientation_to_imu_node
  src/pose_and_orientation_to_imu_node.cpp
)

ament_target_dependencies(pose_and_orientation_to_imu_node
  rclcpp
  sensor_msgs
  geometry_msgs
  nav_msgs
  tf2
  tf2_ros
)

# Install
install(TARGETS
  pose_and_orientation_to_imu_node
  DESTINATION lib/${PROJECT_NAME}
)

# Install launch files
install(DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch
)

ament_package()
