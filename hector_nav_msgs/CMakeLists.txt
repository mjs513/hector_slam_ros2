cmake_minimum_required(VERSION 3.8)
project(hector_nav_msgs)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

set(msg_files
  msg/Info.msg
  msg/MapMetaData.msg
  msg/Map.msg
  msg/Pose.msg
  msg/PoseUpdate.msg
  msg/Trajectory.msg
)

rosidl_generate_interfaces(${PROJECT_NAME}
  ${msg_files}
)

ament_export_dependencies(rosidl_default_runtime)

ament_package()
