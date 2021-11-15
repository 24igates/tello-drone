from djitellopy import tello
import KeyPressModule as kp
from time import sleep

kp.init()
tello = Tello()
tello.connect()


def getKeyboardInput
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    if kp.getKey("LEFT"): lr = -speed
   elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("DOWN"): fb = -speed
    elif kp.getKey("UP"): fb = speed

    if kp.getKey("s"): ud = -speed
    elif kp.getKey("w"): ud = speed

    if kp.getKey("d"): yv = -speed
    elif kp.getKey("a"): yv = speed

    if kp.getKey("q"): tello.land()
    if kp.getKey("e"): tello.takeoff()


    return [ lr, fb, ud, yv]



tello.takeoff()




while True:
    vals = getKeyboardInput()
    tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.5)
