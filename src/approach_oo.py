#!/usr/bin/env python

"""
Simple example of subscribing to sensor messages and publishing
twist messages to the turtlebot.

Author: Nathan Sprague
Version: 1/15/2014

"""
import rospy
import math

# Twist is the message type for sending movement commands.
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class ApproachNode(object):
    """ Class that attempts to maintain a fixed distance from 
    the obstacle ahead. 

    Subscribes to: /scan
    Publishes to: /cmd_vel_mux/input/navi
    """

    def __init__(self):
        """ Set up the node, publishers and subscribers. """
        rospy.init_node('approach')

        rospy.Subscriber('/scan', LaserScan, self.scan_callback)
        self.vel_pub = rospy.Publisher('/cmd_vel_mux/input/navi', Twist) 

        self.target = .75

        # Now enter an infinite loop. Execution will be driven by the
        # callback.
        rospy.spin() 
        

    def scan_callback(self, scan_msg):
        """ Move forward or backward depending on the latest scan. """
        
        twist = Twist()

        # Back up if the scan is bad, or if we are too close. 
        if (math.isnan(scan_msg.ranges[320]) or 
            scan_msg.ranges[320] < self.target):
            twist.linear.x = -.1  
            twist.angular.z = 0   
        else:
            twist.linear.x = .1  
            twist.angular.z = 0   

        rospy.loginfo("Range: {:.3f}".format(scan_msg.ranges[320]))

        self.vel_pub.publish(twist) 
        
if __name__ == "__main__":
    ApproachNode()