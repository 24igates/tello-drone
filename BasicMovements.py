from djitellopy import Tello
from time import sleep


tello = Tello()

tello.connect()

tello.takeoff()
tello.send_rc_control(0,0,50,0)
sleep(3.5)

tello.send_rc_control(0,50,0,0)
sleep(2.7)

tello.send_rc_control(-50,0,0,0)
sleep(2.7)

tello.send_rc_control(0,-50,0,0)
sleep(2.7)

tello.send_rc_control(50,0,0,0)
sleep(2.7)
tello.send_rc_control(0,0,0,0)
tello.flip_forward()

tello.land()
