cmake_minimum_required(VERSION 3.8)
project(hector_mapping)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(std_srvs REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)
find_package(hector_nav_msgs REQUIRED)
find_package(Eigen3 REQUIRED)

include_directories(
  include
  include/hector_slam_lib
  ${EIGEN3_INCLUDE_DIRS}
)

add_executable(hector_mapping_node
  src/main.cpp
  src/HectorMappingRos.cpp
)

ament_target_dependencies(hector_mapping_node
  rclcpp
  sensor_msgs
  geometry_msgs
  nav_msgs
  std_msgs
  std_srvs
  tf2
  tf2_ros
  tf2_geometry_msgs
  hector_nav_msgs
)

install(TARGETS
  hector_mapping_node
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
