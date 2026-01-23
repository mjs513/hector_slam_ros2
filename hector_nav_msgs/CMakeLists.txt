cmake_minimum_required(VERSION 3.8)
project(hector_nav_msgs)

# Required for generating .msg and .srv
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# Dependencies used inside message/service definitions
find_package(geometry_msgs REQUIRED)
find_package(nav_msgs REQUIRED)

# Generate interfaces
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/HectorDebugInfo.msg"
  "msg/HectorIterData.msg"
  "srv/GetRobotTrajectory.srv"
  DEPENDENCIES geometry_msgs nav_msgs
)

ament_export_dependencies(rosidl_default_runtime)

ament_package()
