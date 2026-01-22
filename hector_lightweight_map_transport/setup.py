from setuptools import setup

package_name = "hector_lightweight_map_transport"

setup(
    name=package_name,
    version="0.1.0",
    packages=[package_name, f"{package_name}.nodes", f"{package_name}.msg"],
    data_files=[
        ("share/ament_index/resource_index/packages",
         [f"resource/{package_name}"]),
        (f"share/{package_name}", ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Michael",
    maintainer_email="you@example.com",
    description="Lightweight compressed map transport for Hector SLAM over WiFi.",
    license="BSD",
    entry_points={
        "console_scripts": [
            "map_compressor = hector_lightweight_map_transport.nodes.map_compressor:main",
            "map_decompressor = hector_lightweight_map_transport.nodes.map_decompressor:main",
        ],
    },
)
