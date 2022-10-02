import os
from glob import glob
from setuptools import setup

package_name = 'arm_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='erik',
    maintainer_email='erikcaell@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'arm_node = arm_pkg.arm_node:main',
            'arm_testing_listener = arm_pkg.arm_testing_listener:main',
            'arm_testing_driverstation = arm_pkg.arm_testing_driverstation:main',
        ],
    },
)
