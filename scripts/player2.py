#!/usr/bin/env python2

# SPDX-License-Identifier: BSD-3-Clause
#
#   Copyright (C) 2021 Haruki Shimotori and Ryuichi Ueda. All right reserved.

import rospy
from std_msgs.msg import String 

def cb(msg):
    sub_str = msg.data
    print('player1: ' + sub_str)

if __name__ == '__main__':
    rospy.init_node('player2')
    pub = rospy.Publisher('player2', String, queue_size=1)
    sub = rospy.Subscriber('player1', String, cb)
    rate = rospy.Rate(10)
    print('You are player2. Enjoy chatting!!')
    while not rospy.is_shutdown():
        pub_str = raw_input()
        pub.publish(pub_str)
        rate.sleep()
