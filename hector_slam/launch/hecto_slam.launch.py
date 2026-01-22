from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="hector_mapping",
            executable="hector_mapping",
            name="hector_mapping",
            output="screen",
            parameters=[
                {"map_frame": "map"},
                {"base_frame": "base_link"},
                {"odom_frame": "odom"},
                {"scan_topic": "scan"},
                {"map_resolution": 0.05},
                {"map_size": 2048},
                {"map_start_x": 0.5},
                {"map_start_y": 0.5},
                {"map_multi_res_levels": 2},
                {"update_factor_free": 0.4},
                {"update_factor_occupied": 0.9},
                {"map_update_distance_thresh": 0.4},
                {"map_update_angle_thresh": 0.06},
                {"pub_map_odom_transform": True},
            ],
        ),
    ])
