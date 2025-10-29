#!/usr/bin/env python3

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import LogInfo
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    channel_type =  LaunchConfiguration('channel_type', default='serial')
    front_serial_port = LaunchConfiguration('front_serial_port', default='/dev/front_rplidar')
    back_serial_port = LaunchConfiguration('back_serial_port', default='/dev/back_rplidar')
    serial_baudrate = LaunchConfiguration('serial_baudrate', default='1000000') #for s2 is 1000000
    front_frame_id = LaunchConfiguration('front_frame_id', default='front_rplidar')
    back_frame_id = LaunchConfiguration('back_frame_id', default='back_rplidar')
    inverted = LaunchConfiguration('inverted', default='false')
    angle_compensate = LaunchConfiguration('angle_compensate', default='true')
    scan_mode = LaunchConfiguration('scan_mode', default='DenseBoost')
    front_scan_topic = LaunchConfiguration('front_scan_topic', default='front_scan')
    back_scan_topic = LaunchConfiguration('back_scan_topic', default='back_scan')

    return LaunchDescription([
        DeclareLaunchArgument(
            'channel_type',
            default_value=channel_type,
            description='Specifying channel type of lidar'),

        DeclareLaunchArgument(
            'front_serial_port',
            default_value=front_serial_port,
            description='Specifying usb port to connected lidar'),

        DeclareLaunchArgument(
            'back_serial_port',
            default_value=back_serial_port,
            description='Specifying usb port to connected lidar'),

        DeclareLaunchArgument(
            'serial_baudrate',
            default_value=serial_baudrate,
            description='Specifying usb port baudrate to connected lidar'),
        
        DeclareLaunchArgument(
            'front_frame_id',
            default_value=front_frame_id,
            description='Specifying frame_id of lidar'),
        
        DeclareLaunchArgument(
            'back_frame_id',
            default_value=back_frame_id,
            description='Specifying frame_id of lidar'),

        DeclareLaunchArgument(
            'inverted',
            default_value=inverted,
            description='Specifying whether or not to invert scan data'),

        DeclareLaunchArgument(
            'angle_compensate',
            default_value=angle_compensate,
            description='Specifying whether or not to enable angle_compensate of scan data'),

        DeclareLaunchArgument(
            'scan_mode',
            default_value=scan_mode,
            description='Specifying scan mode of lidar'),
        
        DeclareLaunchArgument(
            'front_scan_topic',
            default_value=front_scan_topic,
            description='Specifying scan mode of lidar'),
        
        DeclareLaunchArgument(
            'back_scan_topic',
            default_value=back_scan_topic,
            description='Specifying scan mode of lidar'),

        Node(
            package='rplidar_ros',
            executable='rplidar_node',
            name='front_rplidar_node',
            parameters=[{'channel_type':channel_type,
                         'serial_port': front_serial_port,
                         'serial_baudrate': serial_baudrate,
                         'frame_id': front_frame_id,
                         'inverted': inverted,
                         'angle_compensate': angle_compensate,
                         'scan_mode': scan_mode,
                         'topic_name': front_scan_topic,
                         'negative_angle_cut_val': -0.9,
                         'positive_angle_cut_val': 0.9
                         }],
            respawn=True,
            respawn_delay=5.0,
            output='screen'),
        
        Node(
            package='rplidar_ros',
            executable='rplidar_node',
            name='back_rplidar_node',
            parameters=[{'channel_type':channel_type,
                         'serial_port': back_serial_port,
                         'serial_baudrate': serial_baudrate,
                         'frame_id': back_frame_id,
                         'inverted': inverted,
                         'angle_compensate': angle_compensate,
                         'scan_mode': scan_mode,
                         'topic_name': back_scan_topic,
                         'negative_angle_cut_val': -0.9,
                         'positive_angle_cut_val': 0.9
                         }],
            respawn=True,
            respawn_delay=5.0,
            output='screen'),
    ])

