cmake_minimum_required(VERSION 3.8)
project(hector_map_tools)

find_package(ament_cmake REQUIRED)

# Install header-only library
install(
  DIRECTORY include/
  DESTINATION include/
)

ament_export_include_directories(include)

ament_package()
