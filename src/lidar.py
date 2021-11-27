#!/usr/bin/env python

# coding = utf-8

import rospy

from sensor_msgs.msg import LaserScan

def scan_callback(msg):

  r1 = msg.ranges[0]
  print "La distance 0 degre: %0.1f" % r1
  r2 = msg.ranges[90]
  print "La distance 90 degre: %0.1f" % r2
  r3 = msg.ranges[180]
  print "La distance 180 degre: %0.1f" % r3
  r4 = msg.ranges[270]
  print "La distance 270 degre: %0.1f" % r4
  r5 = msg.ranges[359]
  print "La distance 360 degre: %0.1f" % r5
 
rospy.init_node('range_ahead')

scan_sub = rospy.Subscriber('scan', LaserScan, scan_callback)

rospy.spin()