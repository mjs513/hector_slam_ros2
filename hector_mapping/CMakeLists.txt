cmake_minimum_required(VERSION 3.8)
project(hector_mapping)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(geometry_msgs REQUIRED)

add_executable(hector_mapping_node
  src/main.cpp
  src/HectorMappingRos.cpp
  src/HectorDebugInfoProvider.cpp
)

ament_target_dependencies(hector_mapping_node
  rclcpp
  nav_msgs
  sensor_msgs
  tf2
  tf2_ros
  geometry_msgs
)

install(TARGETS hector_mapping_node
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
