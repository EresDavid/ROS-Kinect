#!/usr/bin/env python

from launch import LaunchDescription
import launch_ros.actions


def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            package='ros1_bridge', node_executable='sb_robotiq_sp_to_uni', output='screen'),
        launch_ros.actions.Node(
            package='ros1_bridge', node_executable='sb_robotiq_uni_to_sp', output='screen'),
        launch_ros.actions.Node(
            package='ros1_bridge', node_executable='sb_ur_moveit_sp_to_uni', output='screen'),
        launch_ros.actions.Node(
            package='ros1_bridge', node_executable='sb_ur_moveit_uni_to_sp', output='screen'),
        launch_ros.actions.Node(
            package='ros1_bridge', node_executable='sb_ur_updater_sp_to_uni', output='screen'),
        launch_ros.actions.Node(
            package='ros1_bridge', node_executable='sb_ur_updater_uni_to_sp', output='screen')])