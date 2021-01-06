#!/usr/bin/env python2
import rospy
from std_msgs.msg import String 

def cb(msg):
    sub_str = msg.data
    print('player2: ' + sub_str)

if __name__ == '__main__':
    rospy.init_node('player1')
    pub = rospy.Publisher('player1', String, queue_size=1)
    sub = rospy.Subscriber('player2', String, cb)
    rate = rospy.Rate(10)
    print('You are player1. Enjoy chatting!!')
    while not rospy.is_shutdown():
        pub_str = raw_input()
        pub.publish(pub_str)
        rate.sleep()
