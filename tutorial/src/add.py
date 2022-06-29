#!/usr/bin/env python

import rospy

from std_msgs.msg import Int32


class SubscribeInt():    
    def callback1(self, data):
        self.int_1 = data.data
        
    def callback2(self, data):
        self.int_2 = data.data

    def __init__(self):
        self.int_1 = 0
        self.int_2 = 0

        rospy.init_node("subscribing_node", anonymous=False)
        rospy.Subscriber("topic1", Int32, self.callback1)
        rospy.Subscriber("topic2", Int32, self.callback2)
        rate = rospy.Rate(5)

        while not rospy.is_shutdown():
            added_n = self.int_1 + self.int_2
            rospy.loginfo("Addition is : %d", added_n)
            rate.sleep()

        rospy.spin()


if __name__ == "__main__":
    try:
        sub = SubscribeInt()
    except rospy.ROSInterruptException:
        print("Error")