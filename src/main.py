#! /usr/bin/env python
# coding = utf-8
import rospy
from geometry_msgs.msg import Twist

class run():
    def __init__(self):
        rospy.init_node('run', anonymous=False)
        rospy.on_shutdown(self.shutdown) 
        self.cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=1) 
        move = Twist()
        rate = rospy.Rate(1)
    
        while not rospy.is_shutdown():
            move.linear.x = 0.15  # vitesse lineaire
            move.angular.z = 0.00 # vitesse angulaire
            self.cmd_vel.publish(move)
            rate.sleep()
    
    def shutdown(self):
        
        rospy.loginfo("Arreter le robot")
        self.cmd_vel.publish(Twist())
        rospy.sleep(1)


if __name__ == '__main__':
    try:
        run()
    except rospy.ROSInternalException:
        pass