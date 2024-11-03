import gpiozero as gpio
import time

from modules import move, report
from modules import peripherals as prp
from modules.report import report_error

us_sensor = gpio.DistanceSensor(1, 2, max_distance=1, threshold_distance=0.3) # TODO: Figure out which pin to put the distance sensor into
cpu = gpio.CPUTemperature(min_temp=15, max_temp=100)

def main():
    distance_report()
    temperature_report()
    time.sleep(3.5)

def distance_report():
    if us_sensor.distance <= 0.1:
        move.stop()
        report.report_error(f"Robot was {(us_sensor.distance * 10)} centimeters away, moving back {(us_sensor.distance * 10)} centimeters")
        move.move_backward(us_sensor.distance)
    else:
        report.report_error(f"Robot is {(us_sensor.distance * 10)} centimeters away from the nearest object")

def temperature_report():
    report_error(f"CPU is currently {cpu.temperature}º C")
