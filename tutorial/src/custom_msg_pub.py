#!/usr/bin/env python

import rospy
import random

from tutorial.msg import TwoVals


class Publishint():
    def __init__(self):
        rospy.init_node("publishing_node", anonymous=False)
        # declare "TwoVals" topic publisher
        self.pub = rospy.Publisher("combined_topic", TwoVals, queue_size=5)
        rate = rospy.Rate(5)
        # intialize msg object
        msg = TwoVals()

        while not rospy .is_shutdown():
            # pick a random integer from 1 to 20
            n1 = random.randint(1, 20)
            n2 = random.randint(1, 20)
            # insert numbers to msg
            msg.num1 = n1
            msg.num2 = n2
            # publish
            self.pub.publish(msg)
            # print message
            rospy.loginfo("Custom topic is publishing : %d %d", msg.num1, msg.num2)
            rate.sleep()


if __name__ == "__main__":
    try:
        pub = Publishint()
    except rospy.ROSInterruptException:
        print("Error")