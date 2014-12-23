#!/usr/bin/env python
import roslib
roslib.load_manifest("test_teleop")
import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

latest_cmd = Twist()

LINEAR_MULTIPLIER = 0.5
ANGULAR_MULTIPLIER = 0.5

def joy_cb(joy):
	latest_cmd.linear.x = LINEAR_MULTIPLIER * joy.axes[1]
	latest_cmd.angular.z = ANGULAR_MULTIPLIER * joy.axes[0]

if __name__ == '__main__':
	rospy.init_node('test_teleop')
	joy_sub = rospy.Subscriber('/joy', Joy, joy_cb)
	cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

	r = rospy.Rate(25)
	while not rospy.is_shutdown():
		cmd_pub.publish(latest_cmd)
		r.sleep()
