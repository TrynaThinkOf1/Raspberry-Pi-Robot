from gpiozero import Motor
from gpiozero.pins.pigpio import PiGPIOFactory
import time

from modules import report
from modules import peripherals as prp

# Use PiGPIOFactory to avoid conflict with RPi.GPIO if needed
factory = PiGPIOFactory()

# Configure motor pins
motor_left = Motor(forward="BOARD16", backward="BOARD18", pin_factory=factory)  # IN1, IN2 for left motor
motor_right = Motor(forward="BOARD24", backward="BOARD26", pin_factory=factory)   # IN3, IN4 for right motor

def move_forward(cm): #estimated speed is 1cm/second
    motor_left.forward()
    motor_right.forward()
    report.report_update(f"Moving forward {cm}cm")
    time.sleep(cm)
    motor_left.stop()
    motor_right.stop()
    report.report_update("Stopped")

def move_backward(cm):
    motor_left.backward()
    motor_right.backward()
    report.report_update(f"Moving backward {cm}cm")
    time.sleep(cm)
    motor_left.stop()
    motor_right.stop()
    report.report_update("Stopped")

def turn_left(degrees): #estimated turn-rate is 1º/second
    motor_left.backward()
    motor_right.forward()
    report.report_update(f"Turning left {degrees}º")
    time.sleep(degrees)
    motor_left.stop()
    motor_right.stop()
    report.report_update("Stopped")

def turn_right(degrees):
    motor_left.forward()
    motor_right.backward()
    report.report_update(f"Turning right {degrees}º")
    time.sleep(degrees)
    motor_left.stop()
    motor_right.stop()
    report.report_update("Stopped")

def stop():
    motor_left.stop()
    motor_right.stop()
    report.report_update("Stopped")
    prp.red_LED_on()
