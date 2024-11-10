# Raspberry Pi 3 B Remote-Controlled Robot

A Python-powered, remote-controlled robot built on the Raspberry Pi 3 B. This project controls a robot tank through a Python script offering command-line-style control over various movements, functions, and sensors on the robot. This is my very first project combining both software and hardware (other than basic Arduino builds).

## Features

- **Remote-Control Interface**: Issue commands from any device with internet access using a command-line interface.
- **Sensors Integration**: Detect obstacles and measure distances with an ultrasonic sensor.
- **Python-Based**: Fully programmable in Python, making it accessible and highly customizable.

## Technologies

- **Raspberry Pi 3 B**: Acts as the main processor and control unit.
- **Python Script**: Hosts a web server for the remote control interface.
- **Motor Controller**: Controls the robots’s movements.
- **Ultrasonic Sensor**: Detects obstacles and provides data to avoid collisions.

## Repo Info

- **STL Files**: These are the 3d print files.
- **.ai (Adobe Illustrator) Files**: These are laser cut files, they are the best to use so far, make sure to use 3mm/0.125in thick wood.
- **Circuit Diagrams**: These are not accurate _to the Pi GPIO pins_, they are however accurate for all the components.
- **When Changing Pins**: Use a diagram of the Pi GPIO pins _and the gpiozero documentation_ to properly change the code to match your circuit.
