#!/usr/bin/env python3

import rospy
import math

#import messages
import tf2_ros
from tf.transformations import *

#import plan and twist message
from ur5e_control.msg import Plan
from geometry_msgs.msg import Twist
from robot_vision_lectures.msg import SphereParams
from geometry_msgs.msg import Quaternion
from tf2_geometry_msgs import PointStamped
from std_msgs.msg import Bool



sphere_params = SphereParams()

#initialize values
sphere_x = 0
sphere_y = 0
sphere_z = 0
radius = 0
current_pos = [0] * 6

#initialize flags
initialized = False
received_params = False
rqt_toggle = False
pause_toggle = False

def get_sphere_params(data):
	global sphere_params
	global received_params
	global sphere_x
	global sphere_y
	global sphere_z
	
