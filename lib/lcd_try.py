from machine import I2C
import time

l = LCD1602(I2C(1))
l.puts("Hello EaExtin")
