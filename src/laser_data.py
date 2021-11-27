#!/usr/bin/env python
# coding = utf-8
import rospy
from sensor_msgs.msg import LaserScan

def callback(msg):
  print "s1 range ahead: %0.1f" % msg.ranges[0]
  print "s2 range ahead: %0.1f" % msg.ranges[90]
  print "s3 range ahead: %0.1f" % msg.ranges[180]
  print "s4 range ahead: %0.1f" % msg.ranges[270]
  print "s5 range ahead: %0.1f" % msg.ranges[359]

rospy.init_node('laser_data')
sub = rospy.Subscriber('Scan', LaserScan , callback)
rospy.spin()