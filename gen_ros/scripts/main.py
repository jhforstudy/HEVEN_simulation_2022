#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import time

from Database import Database

MAIN_NODE_FPS = 50

def main():
    # Initialize database
    db = Database()
    # Initialize ROS
    rate = rospy.Rate(MAIN_NODE_FPS)
    time.sleep(1)

    while not rospy.is_shutdown():
        rate.sleep()

if __name__ == "__main__":
    main()