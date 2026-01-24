cmake_minimum_required(VERSION 3.8)
project(hector_nav_msgs)

# Core build tools
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# Message dependencies
find_package(geometry_msgs REQUIRED)
find_package(nav_msgs REQUIRED)

# Generate all messages and services in this package
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/HectorDebugInfo.msg"
  "msg/HectorIterData.msg"
  "srv/GetDistanceToObstacle.srv"
  "srv/GetNormal.srv"
  "srv/GetRecoveryInfo.srv"
  "srv/GetRobotTrajectory.srv"
  "srv/GetSearchPosition.srv"
  "srv/ResetMapping.srv"
  DEPENDENCIES geometry_msgs nav_msgs
)

# Export runtime dependencies for downstream packages
ament_export_dependencies(rosidl_default_runtime)

ament_package()
