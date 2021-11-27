#!/usr/bin/env python

# coding = utf-8

import rospy
from geometry_msgs.msg import Twist
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
  
  if r1 < 0.5:
   
    move.linear.x =0.0
    move.angular.z = 1.0
  else:
    move.linear.x = 0.1
    move.angular.z = 0.0
    if r1 < 0.5:
      move.linear.x = 0.0
      move.angular.z = -1.0

  if r2 < 0.1:
    move.linear.x =0.0
    move.angular.z = 0.5
  else:
    move.linear.x = 0.1
    move.angular.z = 0.0
    if r2 < 0.5:
      move.linear.x = 0.0
      move.angular.z = 0.5

  if r4 < 0.1:
    move.linear.x =0.0
    move.angular.z = -0.5
  else:
    move.linear.x = 0.1
    move.angular.z = 0.0
    if r4 < 0.5:
      move.linear.x = 0.0
      move.angular.z = -0.5   
      
  pub.publish(move)
 
move = Twist()
rospy.init_node('obstacle_avoidance_node')
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10) 
scan_sub = rospy.Subscriber('scan', LaserScan, scan_callback)

rospy.spin()