from setuptools import setup

package_name = 'ros2_kinect_driver'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    py_modules=[
        'src.human_joint_pose_publisher'
    ],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Endre and David Eros',
    author_email='endre@todo.com',
    maintainer='Endre and David Eros',
    maintainer_email='endre@todo.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='ROS2 Kinect Stuff Publishers',
    license='',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'src.human_joint_pose_publisher = src.human_joint_pose_publisher:human_joint_pose_publisher'
        ],
    },
)
