cmake_minimum_required(VERSION 3.8)
project(hector_trajectory_server)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(hector_nav_msgs REQUIRED)

include_directories(include)

add_executable(hector_trajectory_server
  src/hector_trajectory_server.cpp
  src/odometry_topic.cpp
)

ament_target_dependencies(hector_trajectory_server
  rclcpp
  tf2
  tf2_ros
  tf2_geometry_msgs
  geometry_msgs
  nav_msgs
  hector_nav_msgs
)

install(TARGETS hector_trajectory_server
  DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
