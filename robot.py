import RPi.GPIO as GPIO
from time import sleep

command_list_help = {
    "w": "move forward until stopped",
    "s": "move backward until stopped",
    "a": "turn left until stopped",
    "d": "turn right until stopped"
}

command_list_valid = {"w", "a", "s", "d"}

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
    while(True):
        command = input(">> ")
        
        if command.lower() == "help":
            for command in command_list_help:
                print(command + " -> " + command_list_help[command] + "\n")
        if command in command_list_valid:
            if command == 'w':
                GPIO.output(in1,GPIO.HIGH)
                GPIO.output(in2,GPIO.LOW)
                
                GPIO.output(in4,GPIO.HIGH)
                GPIO.output(in3,GPIO.LOW)
                print("Forward")
                
            elif command == 's':
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.HIGH)
                
                GPIO.output(in4,GPIO.LOW)
                GPIO.output(in3,GPIO.HIGH)
                print("Backward")
                
            elif command == 'd':
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.HIGH)
                
                GPIO.output(in4,GPIO.LOW)
                GPIO.output(in3,GPIO.LOW)
                print("Right")
                
            elif command == 'a':
                GPIO.output(in1,GPIO.HIGH)
                GPIO.output(in2,GPIO.LOW)
                
                GPIO.output(in4,GPIO.LOW)
                GPIO.output(in3,GPIO.LOW)
                print("Left")
            
            elif command == 'c':
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.LOW)
                
                GPIO.output(in4,GPIO.LOW)
                GPIO.output(in3,GPIO.LOW)
                print("Stop")
        else:
            print("Invalid Command \n")

except KeyboardInterrupt:
  GPIO.cleanup()
  print("GPIO Clean up")

if __name__ == "__main__":
    print("'help' for command list")

