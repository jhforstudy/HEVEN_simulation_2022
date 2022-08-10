#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import cv2
import numpy as np
import time
import os

# Sensor msgs
import sensor_msgs.point_cloud2 as pc2
from morai_msgs.msg import GPSMessage
from sensor_msgs.msg import Imu
from sensor_msgs.msg import Image, CompressedImage
from sensor_msgs.msg import PointCloud2,PointCloud
from geometry_msgs.msg import Point32

# Size of img frame
WIDTH, HEIGHT = 640, 480


class Database():
    def __init__(self):
        rospy.init_node('sensor', anonymous=True)    
        rospy.loginfo("---Initializing sensor node---\n\n\n")
        time.sleep(2)

        # subscribers
        rospy.Subscriber("/imu", Imu, self.imu_callback)
        rospy.Subscriber("/gps", GPSMessage, self.gps_callback)
        rospy.Subscriber("/image_jpeg/compressed", CompressedImage, self.img_callback)
        rospy.Subscriber("/velodyne_points", PointCloud2, self.lidar_callback)

        # imu
        self.imu_orientation = list()
        self.imu_ang_velocity = list()
        self.imu_linear_accel = list()
        # gps
        self.gps_data = list()
        # camera
        self.camera_data = np.empty(shape=[0])

        # publisher for 3D lidar
        self.pc1_pub = rospy.Publisher('/pc1',PointCloud, queue_size=1)

        while not self.camera_data.size == (WIDTH * HEIGHT * 3):
            continue

        rospy.loginfo("---now subscribing sensor data---\n\n\n")
        time.sleep(2)
        
    def imu_callback(self, data):
        self.imu_orientation = [data.orientation.x, data.orientation.y, data.orientation.z, data.orientation.w]
        self.imu_ang_velocity = [data.angular_velocity.x, data.angular_velocity.y, data.angular_velocity.z]
        self.imu_linear_accel = [data.linear_acceleration.x, data.linear_acceleration.y, data.linear_acceleration.z]
        
    def gps_callback(self, data):
        self.gps_data = [data.latitude, data.longitude, data.eastOffset, data.northOffset]
        
    def img_callback(self, data):
        np_arr = np.fromstring(data.data, np.uint8)
        img_bgr = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        self.camera_data = img_bgr.copy()
        winname = "Image window"
        cv2.moveWindow(winname, 40, 30)
        cv2.imshow(winname, img_bgr)
        cv2.waitKey(1)

    def lidar_callback(self, data):
        pc1_msg=PointCloud()
        for p in pc2.read_points(data, field_names = ("x", "y", "z"), skip_nans=True):
            tmp_point=Point32()
            tmp_point.x=p[0]
            tmp_point.y=p[1]
            tmp_point.z=p[2]
            pc1_msg.points.append(tmp_point)

        pc1_msg.header.frame_id=data.header.frame_id
        pc1_msg.header.stamp=data.header.stamp
        self.pc1_pub.publish(pc1_msg)
        

if __name__ == "__main__":
    try:
        db = Database()
        rate = rospy.Rate(100)
        while not rospy.is_shutdown():
            print("==================================")
            print(db.imu_orientation)
            print(db.imu_ang_velocity)
            print(db.imu_linear_accel)
            print(db.gps_data)
            print("==================================")
            rate.sleep()
        
        rospy.spin()

    except rospy.ROSInterruptException:
        rospy.loginfo("Error!!!")