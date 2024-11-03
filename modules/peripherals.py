from gpiozero import LED, Buzzer
import time

#LEDs
red_led = LED(1) # TODO: Figure out which pin to put the red LED into
green_led = LED(2) # TODO: Figure out which pin to put the green LED into
white_led = LED(3) # TODO: Figure out which pin to put the white LED into

def red_LED():
    red_led.toggle()
def white_LED():
    white_led.toggle()

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

def beep(interval):
    buzzer.beep(interval, interval)
