cmake_minimum_required(VERSION 3.8)
project(hector_imu_attitude_to_tf)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)

include_directories(include)

add_executable(imu_attitude_to_tf_node
  src/imu_attitude_to_tf_node.cpp
)

ament_target_dependencies(imu_attitude_to_tf_node
  rclcpp
  sensor_msgs
  geometry_msgs
  tf2
  tf2_ros
)

install(TARGETS
  imu_attitude_to_tf_node
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
