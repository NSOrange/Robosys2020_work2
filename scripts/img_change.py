#!/usr/bin/env python3
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

bridge = CvBridge()

def gray(msg):
        orig = bridge.imgmsg_to_cv2(msg, "bgr8")
        img = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
        gray_img = bridge.cv2_to_imgmsg(img, "mono8")
        pub = rospy.Publisher('image_gray', Image, queue_size=10)
        pub.publish(gray_img)


def start_node():
    rospy.init_node('img_change')
    sub = rospy.Subscriber('/cv_camera/image_raw', Image, gray)
    rospy.spin()


if __name__ == '__main__':
        start_node()
