cmake_minimum_required(VERSION 3.8)
project(hector_nav_msgs)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# Only include this if you actually have .msg files
# rosidl_generate_interfaces(${PROJECT_NAME}
#   "msg/Trajectory.msg"
# )

ament_export_dependencies(rosidl_default_runtime)
ament_package()


