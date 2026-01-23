from setuptools import setup

package_name = 'hector_lightweight_map_transport'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Michael',
    maintainer_email='you@example.com',
    description='Lightweight map transport utilities (Python + C++).',
    license='BSD',
    entry_points={
        'console_scripts': [
            'map_compressor = hector_lightweight_map_transport.map_compressor:main',
        ],
    },
)
