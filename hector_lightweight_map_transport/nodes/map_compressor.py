import zlib

import rclpy
from rclpy.node import Node

from nav_msgs.msg import OccupancyGrid
from hector_lightweight_map_transport.msg import CompressedMap


class MapCompressor(Node):
    def __init__(self):
        super().__init__("map_compressor")

        self.map_sub = self.create_subscription(
            OccupancyGrid,
            "map",
            self.map_callback,
            10,
        )

        self.pub = self.create_publisher(
            CompressedMap,
            "map_compressed",
            10,
        )

        self.codec = "zlib"

    def map_callback(self, msg: OccupancyGrid):
        # Convert int8[] to bytes
        raw = bytes((x & 0xFF for x in msg.data))

        compressed = zlib.compress(raw, level=6)

        out = CompressedMap()
        out.header = msg.header
        out.info = msg.info
        out.codec = self.codec
        out.data = list(compressed)

        self.pub.publish(out)


def main(args=None):
    rclpy.init(args=args)
    node = MapCompressor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
