cmake_minimum_required(VERSION 3.8)
project(hector_trajectory_server)

# Dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)

# Executable
add_executable(hector_trajectory_server_node
  src/hector_trajectory_server.cpp
  src/odometry_topic.cpp
)

ament_target_dependencies(hector_trajectory_server_node
  rclcpp
  nav_msgs
  geometry_msgs
  tf2
  tf2_ros
  tf2_geometry_msgs
)

# Install
install(TARGETS
  hector_trajectory_server_node
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
