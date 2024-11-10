import RPi.GPIO as GPIO
import keyboard
from time import sleep

keyboard.on_press(on_key_press)
keyboard.on_release(on_key_release)

keyboard.wait('esc')

GPIO.setwarnings(False)

# Right Motor
in1 = 17
in2 = 27
en_a = 4
# Left Motor
in3 = 5
in4 = 6
en_b = 13


GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en_a,GPIO.OUT)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en_b,GPIO.OUT)

q=GPIO.PWM(en_a,100)
p=GPIO.PWM(en_b,100)
p.start(75)
q.start(75)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)

try:    
    def move_forward():
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        
        GPIO.output(in4,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        print("Forward")
    
    def move_backward():
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        print("Backward")
    
    def turn_right():
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        
        GPIO.output(in4,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        print("Right")
    
    def turn_left():
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        print("Left")
    
    def stop_movement():
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        print("Stop")

except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO Clean up")

def on_key_press(event):
    if event.name == 'w':
        move_forward()
    elif event.name == 's':
        move_backward()
    elif event.name == 'a':
        turn_left()
    elif event.name == 'd':
        turn_right()

def on_key_release(event):
    if event.name in {'w', 's', 'a', 'd'}:
        stop_movement()

if __name__ == "__main__":
    print("'help' for command list")

