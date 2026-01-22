cmake_minimum_required(VERSION 3.8)
project(hector_lightweight_map_transport)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rosidl_default_generators REQUIRED)

set(msg_files
  "hector_lightweight_map_transport/msg/CompressedMap.msg"
)

rosidl_generate_interfaces(${PROJECT_NAME}
  ${msg_files}
)

ament_export_dependencies(rosidl_default_runtime)

ament_python_install_package(${PROJECT_NAME})

install(
  PROGRAMS
    hector_lightweight_map_transport/nodes/map_compressor.py
    hector_lightweight_map_transport/nodes/map_decompressor.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
