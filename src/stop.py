#!/usr/bin/env python  

import rospy
# importer main Python pour ROS lib
from geometry_msgs.msg import Twist
from math import pi
# importer la sorte de message Twist dans la lib de geometry_msgs
class OutAndBack():
    def __init__(self):
        # le nom de noeud
        rospy.init_node('out_and_back', anonymous=False)
        # Arreter le noeud en appuyant crtl+c
        rospy.on_shutdown(self.shutdown) 
        # Identifier la sorte de message Twist dans le /cmd_vel et controler la vitesse de robot
        self.cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=1) 
        rate = 50 
        # Parametrer la frequence d'actualisation par 50Hz
        r = rospy.Rate(rate) 
        # Vitesse lineaire
        linear_speed = 0.2 
        # La distance entre la cible
        goal_distance = 1.0
        # Le temps d'arriver la cible
        linear_duration = goal_distance / linear_speed
        # Vitesse angualire 1.0rad/s
        # angular_speed = 0.0 
        # L'angle est Pi(180 degre)
        # goal_angle = pi
        # Le temps de rotation
        # angular_duration = goal_angle / angular_speed

        # 2 boucles
        for i in range(2):
            # Initialiser la commande du movement
            move_cmd = Twist()

            # Parametrer la vitesse d'avancer
            move_cmd.linear.x = linear_speed
            # Le robot avance dans un delais
            ticks = int(linear_duration * rate)
            for t in range(ticks):
                self.cmd_vel.publish(move_cmd)
                r.sleep()

            # Envoyer un NULL message de Twist pour arreter le robot
            move_cmd = Twist()
            self.cmd_vel.publish(move_cmd)
            rospy.sleep(1)

            # move_cmd.angular.z = angular_speed
            # Le robot commence a tourner 180 degre dans un delais
            # ticks = int(goal_angle * rate)
            # for t in range(ticks):
            #     self.cmd_vel.publish(move_cmd)
            #     r.sleep()

            # arreter
            move_cmd = Twist()
            self.cmd_vel.publish(move_cmd)
            rospy.sleep(1)

        # arreter apres 2 boucles
        self.cmd_vel.publish(Twist())

        # shutdown(self) peut arreter le robot manuellement
    def shutdown(self):
        # Toujours arreter le robot quand eteindre le noeud
        rospy.loginfo("Arreter le robot")
        self.cmd_vel.publish(Twist())
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        OutAndBack()
    except:
        rospy.loginfo("Le noeud est termine.")