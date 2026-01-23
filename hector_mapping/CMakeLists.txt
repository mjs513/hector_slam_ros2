cmake_minimum_required(VERSION 3.8)
project(hector_mapping)

# ---------------------------------------------------------
# Dependencies
# ---------------------------------------------------------
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(Eigen3 REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# ---------------------------------------------------------
# Message + Service generation
# ---------------------------------------------------------
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/HectorDebugInfo.msg"
  "msg/HectorIterData.msg"
  "srv/ResetMapping.srv"
  DEPENDENCIES geometry_msgs nav_msgs
)

ament_export_dependencies(rosidl_default_runtime)

# ---------------------------------------------------------
# Include directories
# ---------------------------------------------------------
include_directories(
  include
  ${EIGEN3_INCLUDE_DIRS}
)

# ---------------------------------------------------------
# C++ executable
# ---------------------------------------------------------
add_executable(hector_mapping_node
  src/main.cpp
  src/HectorMappingRos.cpp
  src/PoseInfoContainer.cpp
)

ament_target_dependencies(hector_mapping_node
  rclcpp
  sensor_msgs
  nav_msgs
  geometry_msgs
  tf2
  tf2_ros
)

# ---------------------------------------------------------
# Install targets
# ---------------------------------------------------------
install(TARGETS
  hector_mapping_node
  DESTINATION lib/${PROJECT_NAME}
)

# Install headers
install(DIRECTORY include/
  DESTINATION include/
)

# Install messages/services
install(DIRECTORY msg/
  DESTINATION share/${PROJECT_NAME}/msg
)

install(DIRECTORY srv/
  DESTINATION share/${PROJECT_NAME}/srv
)

# Install launch files
install(DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch
  OPTIONAL
)

ament_package()
