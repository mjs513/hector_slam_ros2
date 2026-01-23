cmake_minimum_required(VERSION 3.8)
project(hector_nav_msgs)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(nav_msgs REQUIRED)

# Message + service generation
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

ament_export_dependencies(rosidl_default_runtime)

# Install interface files
install(DIRECTORY msg/
  DESTINATION share/${PROJECT_NAME}/msg
)

install(DIRECTORY srv/
  DESTINATION share/${PROJECT_NAME}/srv
)

ament_package()
