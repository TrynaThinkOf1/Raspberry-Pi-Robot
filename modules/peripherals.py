from gpiozero import LED, Buzzer
import time

from modules import report

#LEDs
red_led = LED(1) # TODO: Figure out which pin to put the red LED into
green_led = LED(2) # TODO: Figure out which pin to put the green LED into
white_led = LED(3) # TODO: Figure out which pin to put the white LED into

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
buzzer = Buzzer(3) # TODO 3: Figure out which pin to put the Piezo butter into

def buzz():
    buzzer.toggle()
    if buzzer.value == 0:
        report.report_update("Buzzer is off.")
    else:
        report.report_update("Buzzer is on.")

def beep(interval):
        buzzer.beep(interval, interval, 8)
