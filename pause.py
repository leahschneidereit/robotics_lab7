#!/usr/bin/env python3

import rospy

from std_msgs.msg import Bool

if __name__ == "__main__":
	rospy.init_node('pause_node', anonymous = True)
	pause_pub = rospy.Publisher('/pause_toggle',Bool, queue_size = 1)
	pause_pub.publish(Bool(True))
