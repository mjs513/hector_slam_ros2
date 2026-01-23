#include <rclcpp/rclcpp.hpp>
#include <nav_msgs/msg/occupancy_grid.hpp>

class LightweightMapTransport : public rclcpp::Node
{
public:
  LightweightMapTransport()
  : Node("lightweight_map_transport")
  {
    // Parameters
    this->declare_parameter("map_topic", "/map");
    this->declare_parameter("output_topic", "/map_throttled");
    this->declare_parameter("publish_rate", 1.0);

    std::string map_topic = this->get_parameter("map_topic").as_string();
    std::string output_topic = this->get_parameter("output_topic").as_string();
    double publish_rate = this->get_parameter("publish_rate").as_double();

    map_sub_ = this->create_subscription<nav_msgs::msg::OccupancyGrid>(
      map_topic, 10,
      std::bind(&LightweightMapTransport::mapCallback, this, std::placeholders::_1));

    map_pub_ = this->create_publisher<nav_msgs::msg::OccupancyGrid>(output_topic, 10);

    timer_ = this->create_wall_timer(
      std::chrono::milliseconds(static_cast<int>(1000.0 / publish_rate)),
      std::bind(&LightweightMapTransport::publishMap, this));
  }

private:
  void mapCallback(const nav_msgs::msg::OccupancyGrid::SharedPtr msg)
  {
    latest_map_ = msg;
  }

  void publishMap()
  {
    if (latest_map_) {
      map_pub_->publish(*latest_map_);
    }
  }

  rclcpp::Subscription<nav_msgs::msg::OccupancyGrid>::SharedPtr map_sub_;
  rclcpp::Publisher<nav_msgs::msg::OccupancyGrid>::SharedPtr map_pub_;
  rclcpp::TimerBase::SharedPtr timer_;

  nav_msgs::msg::OccupancyGrid::SharedPtr latest_map_;
};

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<LightweightMapTransport>());
  rclcpp::shutdown();
  return 0;
}
