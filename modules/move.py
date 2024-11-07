from gpiozero import Motor, PWMOutputDevice
from gpiozero.pins.pigpio import PiGPIOFactory
import time

from modules import report
from modules import peripherals as prp

# Use PiGPIOFactory to avoid conflict with RPi.GPIO if needed
factory = PiGPIOFactory()

# Configure motor pins
ena = PWMOutputDevice("BOARD36", pin_factory=factory)
enb = PWMOutputDevice("BOARD38", pin_factory=factory)
motor_left = Motor(forward="BOARD16", backward="BOARD18", pin_factory=factory)
motor_right = Motor(forward="BOARD24", backward="BOARD26", pin_factory=factory)

def move_forward(cm): #estimated speed is 10cm/second
    ena.value = 1.0
    enb.value = 1.0
    motor_left.forward()
    motor_right.forward()
    report.report_update(f"Moving forward {cm}cm")
    time.sleep(cm/10)
    motor_left.stop()
    motor_right.stop()
    ena.value = 0.0
    enb.value = 0.0
    report.report_update("Stopped")

def move_backward(cm):
    ena.value = 0.8
    enb.value = 0.8
    motor_left.backward()
    motor_right.backward()
    report.report_update(f"Moving backward {cm}cm")
    time.sleep(cm/10)
    motor_left.stop()
    motor_right.stop()
    ena.value = 0.0
    enb.value = 0.0
    report.report_update("Stopped")

def turn_left(degrees): #estimated turn-rate is 10º/second
    ena.value = 1.0
    enb.value = 1.0
    motor_left.backward()
    motor_right.forward()
    report.report_update(f"Turning left {degrees}º")
    time.sleep(degrees/10)
    motor_left.stop()
    motor_right.stop()
    ena.value = 0.0
    enb.value = 0.0
    report.report_update("Stopped")

def turn_right(degrees):
    ena.value = 1.0
    enb.value = 1.0
    motor_left.forward()
    motor_right.backward()
    report.report_update(f"Turning right {degrees}º")
    time.sleep(degrees/10)
    motor_left.stop()
    motor_right.stop()
    ena.value = 0.0
    enb.value = 0.0
    report.report_update("Stopped")

def stop():
    ena.value = 0.0
    enb.value = 0.0
    motor_left.stop()
    motor_right.stop()
    report.report_update("Stopped")
    prp.red_LED_on()
