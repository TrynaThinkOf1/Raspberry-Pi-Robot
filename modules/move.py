import gpiozero as gpio
import time

from modules import peripherals as prp

robot = gpio.Robot(left=gpio.Motor(1, 2), right=gpio.Motor(3, 4)) # TODO: Figure out which pin to put the motors into

def move_forward(cm): #ESTIMATED RATE IS 1CM/SECOND
    prp.green_LED()
    robot.forward()
    time.sleep(cm)
    prp.green_LED()
    robot.stop()

def move_backward(cm):
    prp.green_LED()
    robot.backward()
    time.sleep(cm)
    prp.green_LED()
    robot.stop()

def move_left(cm):
    prp.green_LED()
    robot.left()
    time.sleep(cm)
    prp.green_LED()
    robot.stop()

def move_right(cm):
    prp.green_LED()
    robot.right()
    time.sleep(cm)
    prp.green_LED()
    robot.stop()

def stop():
    prp.red_LED_on()
    robot.stop()
