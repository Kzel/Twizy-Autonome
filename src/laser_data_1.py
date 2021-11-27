#!/usr/bin/env python
# coding = utf-8
import rospy
from sensor_msgs.msg import LaserScan

def callback(msg):
  print "La distance en 0 degre: %0.1f" % msg.ranges[0]
  print "La distance en 90 degre: %0.1f" % msg.ranges[90]
  print "La distance en 180 degre: %0.1f" % msg.ranges[180]
  print "La distance en 270 degre: %0.1f" % msg.ranges[270]

rospy.init_node('laser_data')
sub = rospy.Subscriber('Scan', LaserScan , callback)
rospy.spin()