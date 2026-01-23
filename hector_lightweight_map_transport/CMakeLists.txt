cmake_minimum_required(VERSION 3.8)
project(hector_lightweight_map_transport)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)

include_directories(include)

add_executable(lightweight_map_transport_node
  src/lightweight_map_transport.cpp
)

ament_target_dependencies(lightweight_map_transport_node
  rclcpp
  nav_msgs
  geometry_msgs
)

install(TARGETS
  lightweight_map_transport_node
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
