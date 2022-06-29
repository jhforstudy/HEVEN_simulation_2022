#!/usr/bin/env python

import rospy
import random

from std_msgs.msg import Int32


class Publishint():
    def __init__(self):
        rospy.init_node("publishing_node", anonymous=False)
        self.pub1 = rospy.Publisher("topic1", Int32, queue_size=5)
        self.pub2 = rospy.Publisher("topic2", Int32, queue_size=5)
        rate = rospy.Rate(5)

        while not rospy .is_shutdown():
            # pick a random integer from 1 to 20
            n1 = random.randint(1, 20)
            n2 = random.randint(1, 20)
            # publish
            self.pub1.publish(n1)
            self.pub2.publish(n2)
            # print message
            rospy.loginfo("Two topics are publishing : %d %d", n1, n2)
            rate.sleep()


if __name__ == "__main__":
    try:
        pub = Publishint()
    except rospy.ROSInterruptException:
        print("Error")