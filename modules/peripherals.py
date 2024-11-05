from gpiozero import LED, Buzzer
import time

from modules import report
from modules.report import report_update

#LEDs
red_led = LED("BOARD8") 
green_led = LED("BOARD10")
white_led = LED("BOARD12")

def red_LED():
    red_led.toggle()
    if red_led.value == 0:
        report.report_update("Red LED is off.")
    else:
        report.report_update("red LED is on.")
def white_LED():
    white_led.toggle()
    if white_led.value == 0:
        report.report_update("White LED is off.")
    else:
        report.report_update("White LED is on.")

def green_LED(): #NOT FOR COMMAND USE, ONLY FOR SYSTEM USE
    green_led.toggle()
def red_LED_on(): #FOR SYSTEM USE
    red_led.on()
    time.sleep(3.5)
    red_led.off()

#Buzzer
buzzer = Buzzer("BOARD32")

def buzz():
    buzzer.toggle()
    if buzzer.value == 0:
        report.report_update("Buzzer is off.")
    else:
        report.report_update("Buzzer is on.")

def beep(interval):
        buzzer.beep(interval, interval, 8)
        report.report_update("Buzzer beeping...")
