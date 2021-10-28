from djitellopy import Tello
from time import sleep

feet = 30
tello = Tello()

tello.connect()

sleep(2)
tello.takeoff()

tello.move_up(100)

sleep(2)
tello.move_forward(10*feet)

sleep(2)
tello.move_left(10)

sleep(2)
tello.move_back(10)

sleep(2)
tello.move_right(10)

sleep(2)
tello.flip_forward()


tello.land()
