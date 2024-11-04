# Raspberry Pi 4 Remote-Controlled Robot Tank

A Python-powered, remote-controlled robot tank built on the Raspberry Pi 4. This project controls a robot tank through a Python Flask web interface, offering command-line-style control over various movements, functions, and sensors on the tank. This is my very first project combining both software and hardware (other than basic Arduino builds).

## Features

- **Remote-Control Interface**: Issue commands from any device with internet access using a command-line interface served through Flask.
- **Real-Time Control**: Control forward, backward, left, right movements, and speed adjustments.
- **Video Streaming**: Real-time video feed from the robot’s PiCam module for visual feedback and navigation.
- **Sensors Integration**: Detect obstacles and measure distances with an ultrasonic sensor.
- **Python-Based**: Fully programmable in Python, making it accessible and highly customizable.

## Technologies

- **Raspberry Pi 4**: Acts as the main processor and control unit.
- **Python Flask**: Hosts a web server for the remote control interface.
- **Motor Controller**: Controls the tank’s movements.
- **Ultrasonic Sensor**: (Optional) Detects obstacles and provides data to avoid collisions.
- **Pi Camera**: Streams live video for remote viewing.
