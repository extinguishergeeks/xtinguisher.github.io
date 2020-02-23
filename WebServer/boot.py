try:
  import usocket as socket
except:
  import socket
  

import network
import machine
from machine import Pin, ADC, PWM, I2C
import math
import time
import servo
import esp
esp.osdebug(None)

import gc
AIN1 = Pin(15,Pin.OUT)
AIN2 = Pin(2,Pin.OUT)
BIN1 = Pin(0,Pin.OUT)
BIN2 = Pin(4,Pin.OUT)

PWMPinA = PWM(Pin(16), freq = 980)
PWMPinB = PWM(Pin(17), freq = 980)

i2c=I2C(-1, scl=Pin(22), sda=Pin(21))
servo = servo.Servos(i2c)
servo.position(0, degrees=75)
servo.position(1, degrees=75)
servo.position(2, degrees=90)
servo.position(3, degrees=90)
def ModeStop():
    AIN1.off()
    AIN2.off()
    BIN1.off()
    BIN2.off()
    
def ModeForward():
    AIN1.on()
    AIN2.off()
    BIN1.on()
    BIN2.off()
    
def ModeBackward():
    AIN1.off()
    AIN2.on()
    BIN1.off()
    BIN2.on()
    
def ModeRight():
    AIN1.on()
    AIN2.off()
    BIN1.off()
    BIN2.on()
    
def ModeLeft():
    AIN1.off()
    AIN2.on()
    BIN1.on()
    BIN2.off()
    
def OpenClose():
    servo.position(0,0)
def OpenClose1():
    servo.position(0,180)   
def ForBack():
    servo.position(1,0)
def ForBack1():
    servo.position(1,90)
def ForBack2():
    servo.position(1,180)    
def UpDown():
    servo.position(2,0)
def UpDown1():
    servo.position(2,90)
def UpDown2():
    servo.position(2,180)    
def LeftRight():
    servo.position(3,0)
def LeftRight1():
    servo.position(3,90)
def LeftRight2():
    servo.position(3,180)
    
gc.collect()

ssid = 'EaExtin'
password = ''
robot_state = "Stop"

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)
ap.ifconfig(('192.168.22.1', '255.255.255.0', '192.168.22.1', '8.8.8.8'))


while ap.active() == False:
  pass

print('Connection successful')
print(ap.ifconfig())



def web_page():
  
  html = """
  <html>
  <head> 
  <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> 
  <style>
  html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}
  .button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; 
  text-decoration: none; font-size: 30px;
  margin: 2px; cursor: pointer;}
  .buttonStop{background-color: red;}
  .rotateimg180{-webkit-transform:rotate(180deg);
  -moz-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  -o-transform: rotate(180deg);
  transform: rotate(180deg);}
   </style>
  <script src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js\"></script>
  <script src="https://obniz.io/js/jquery-3.2.1.min.js"></script>
  <script src="https://unpkg.com/obniz@3.3.0/obniz.js"></script>
  </head>
  <body> 
  <h1>ESP Web Server</h1>
  <img class="stream" src=http://192.168.22.2:81 class="rotateimg180"/stream>
  <p>Robot state: <strong>""" + robot_state + """</strong></p>
  <p><a href="/?robot=stop"><button class="button buttonStop">STOP</button></a></p>
  <p><a href="/?robot=forward"><button class="button">FORWARD</button></a></p>
  <p><a href="/?robot=backward"><button class="button">BACKWARD</button></a></p>
  <p><a href="/?robot=right"><button class="button">RIGHT</button></a></p>
  <p><a href="/?robot=left"><button class="button">LEFT</button></a></p>
  <p>Open and Close</p>
  <p><a href="/?Req1=0\"><button class="button">0 degrees</button></a>
     <a href="/?Req1=90\"><button class="button">45 degrees</button></a>
  <p>Up and Down</p>   
  <p><a href="/?Req2=0\"><button class="button">0 degrees</button></a>
     <a href="/?Req2=90\"><button class="button">90 degrees</button></a>
     <a href="/?Req2=180\"><button class="button">180 degrees</button></a></p>
  <p>Forward and Backward</p>   
  <p><a href="/?Req3=0\"><button class="button">0 degrees</button></a>
     <a href="/?Req3=90\"><button class="button">90 degrees</button></a>
     <a href="/?Req3=180\"><button class="button">180 degrees</button></a></p>
  <P>Left and Right</p>  
  <p><a href="/?Req4=0\"><button class="button">0 degrees</button></a>
     <a href="/?Req4=90\"><button class="button">90 degrees</button></a>
     <a href="/?Req4=180\"><button class="button">180 degrees</button></a></p>     
  </body>
  </html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  robot_stop = request.find('/?robot=stop')
  robot_forward = request.find('/?robot=forward')
  robot_backward = request.find('/?robot=backward')
  robot_right = request.find('/?robot=right')
  robot_left = request.find('/?robot=left')
  oc_0 = request.find('/?Req1=0')
  oc_90 = request.find('/?Req1=90')
  up_0 = request.find('/?Req2=0')
  up_90 = request.find('/?Req2=90')
  up_180 = request.find('/?Req2=180')
  fb_0 = request.find('/?Req3=0')
  fb_90 = request.find('/?Req3=90')
  fb_180 = request.find('/?Req3=180')
  lr_0 = request.find('/?Req4=0')
  lr_90 = request.find('/?Req4=90')
  lr_180 = request.find('/?Req4=180')
  if oc_0 == 6:
    OpenClose()
  if oc_90 == 6:
    OpenClose1()
  
  if up_0 == 6:
    UpDown()
  if up_90 == 6:
    UpDown1()
  if up_180 == 6:
    UpDown2()
  if fb_0 == 6:
    ForBack()
  if fb_90 == 6:
    ForBack1()
  if fb_180 == 6:
    ForBack2()
  if lr_0 == 6:
    LeftRight()
  if lr_90 == 6:
    LeftRight1()
  if lr_180 == 6:
    LeftRight2()
  if robot_stop == 6:
    print('robot stopping...')
    robot_state = "Stop"
    ModeStop()
  if robot_forward == 6:
    print('robot advancing forward...')
    robot_state = "Forward"
    ModeForward()
  if robot_backward == 6:
    print('robot retreating backward...')
    robot_state = "Backward"
    ModeBackward()
  if robot_right == 6:
    print('robot turning right...')
    robot_state = "Right"
    ModeRight()
  if robot_left == 6:
    print('robot turning left...')
    robot_state = "Left"
    ModeLeft()
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()















































































































