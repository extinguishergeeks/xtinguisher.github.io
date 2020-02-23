import servo
from machine import I2C, Pin
import time

i2c = I2C(-1, scl=Pin(22), sda=Pin(21))

# Create a simple PCA9685 class instance.
servo = servo.Servos(i2c)

servo.position(0, degrees=100)

#time.sleep(1)
#servo.position(0, degrees=150)