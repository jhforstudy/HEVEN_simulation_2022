#!/usr/bin/env python

import rospy

from tutorial.msg import TwoVals


class SubscribeInt():    
    def callback(self, data):
        self.int_1 = data.num1
        self.int_2 = data.num2

    def __init__(self):
        self.int_1 = 0
        self.int_2 = 0

        rospy.init_node("subscribing_node", anonymous=False)
        # subscribe "TwoVals" topic
        rospy.Subscriber("combined_topic", TwoVals, self.callback)
        rate = rospy.Rate(5)

        while not rospy.is_shutdown():
            # add two values
            added_n = self.int_1 + self.int_2
            # print
            rospy.loginfo("Addition is : %d", added_n)
            rate.sleep()

        rospy.spin()


if __name__ == "__main__":
    try:
        sub = SubscribeInt()
    except rospy.ROSInterruptException:
        print("Error")