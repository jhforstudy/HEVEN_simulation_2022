#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import time

from Database import Database

MAIN_NODE_FPS = 100

def main():
    # Initialize database
    db = Database()
    # Initialize ROS
    rate = rospy.Rate(MAIN_NODE_FPS)
    time.sleep(1)

    while not rospy.is_shutdown():
        print("==================================")
        print(db.imu_orientation)
        print(db.imu_ang_velocity)
        print(db.imu_linear_accel)
        print(db.gps_data)
        print("==================================")
        rate.sleep()

if __name__ == "__main__":
    main()