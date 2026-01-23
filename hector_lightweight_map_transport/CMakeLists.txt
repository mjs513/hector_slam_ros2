cmake_minimum_required(VERSION 3.8)
project(hector_lightweight_map_transport)

# ---------------------------------------------------------
# Dependencies
# ---------------------------------------------------------
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# ---------------------------------------------------------
# Message generation
# ---------------------------------------------------------
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/CompressedMap.msg"
  DEPENDENCIES nav_msgs geometry_msgs
)

ament_export_dependencies(rosidl_default_runtime)

# ---------------------------------------------------------
# C++ executable
# ---------------------------------------------------------
add_executable(lightweight_map_transport_node
  src/lightweight_map_transport_node.cpp
)

ament_target_dependencies(lightweight_map_transport_node
  rclcpp
  sensor_msgs
  nav_msgs
  geometry_msgs
  tf2
  tf2_ros
)

install(TARGETS
  lightweight_map_transport_node
  DESTINATION lib/${PROJECT_NAME}
)

# ---------------------------------------------------------
# Python module + entry points
# ---------------------------------------------------------
ament_python_install_package(${PROJECT_NAME})

install(PROGRAMS
  nodes/map_compressor.py
  DESTINATION lib/${PROJECT_NAME}
)

# ---------------------------------------------------------
# Install message files
# ---------------------------------------------------------
install(DIRECTORY msg/
  DESTINATION share/${PROJECT_NAME}/msg
)

# ---------------------------------------------------------
# Install launch files (if added later)
# ---------------------------------------------------------
install(DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch
  OPTIONAL
)

ament_package()
