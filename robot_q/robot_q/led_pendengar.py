import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
import RPi.GPIO as GPIO
import time


class LedSubscriber(Node):

    def __init__(self):
        super().__init__('led_pendengar')
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.listener_callback,
            10)       
        led_r=21
        led_g=4
        led_b=14

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(led_r, GPIO.OUT)
        GPIO.setup(led_g, GPIO.OUT)
        GPIO.setup(led_b, GPIO.OUT)

        self.lr = led_r
        self.lg = led_g
        self.lb = led_b

    def listener_callback(self, msg):
        
        arah_kanan = (msg.linear.x + msg.angular.z)/2
        arah_kiri = (msg.linear.x - msg.angular.z)/2

        print (arah_kanan, " / ", arah_kiri)

        #nyala lampu kanan kiri tengah
        GPIO.output(self.lr, arah_kanan<0)
        GPIO.output(self.lg, arah_kiri<0)
        GPIO.output(self.lb, arah_kanan==0.25 and arah_kiri==0.25)

        #stop
        if arah_kanan==0.0 and arah_kiri==0.0:
            GPIO.output(self.lr, GPIO.LOW)
            GPIO.output(self.lg, GPIO.LOW)
            GPIO.output(self.lb, GPIO.LOW)


def main(args=None):
    rclpy.init(args=args)

    led_subscriber = LedSubscriber()

    rclpy.spin(led_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    led_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
