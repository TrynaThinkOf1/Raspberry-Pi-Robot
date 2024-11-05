import time
import requests as rq

from modules import move, report
from modules import peripherals as prp

tries = 10

rec_cmd = rq.get('http://192.168.50.77:5000/rec_cmd').content.decode('utf-8')

def main():
    while True:
        command_check()
        time.sleep(1.5)

def command_check():
    #movement
    if rec_cmd[0:4] == 'fwd:':
        try:
            move.move_forward(float(rec_cmd[4:]))
        except Exception as error:
            if tries > 0:
                report.report_error(error)
                main()

    if rec_cmd[0:4] == 'bkd:':
        try:
            move.move_backward(float(rec_cmd[4:]))
        except Exception as error:
            if tries > 0:
                report.report_error(error)
                main()

    if rec_cmd[0:5] == 'left:':
        try:
            move.turn_left(float(rec_cmd[5:]))
        except Exception as error:
            if tries > 0:
                report.report_error(error)
                main()

    if rec_cmd[0:6] == 'right:':
        try:
            move.turn_right(float(rec_cmd[6:]))
        except Exception as error:
            if tries > 0:
                report.report_error(error)
                main()

    #LEDs
    if rec_cmd == 'red_LED':
        try:
            prp.red_LED()
        except Exception as error:
            if tries > 0:
                report.report_error(error)
                main()
    if rec_cmd == 'white_LED':
        try:
            prp.white_LED()
        except Exception as error:
            if tries > 0:
                report.report_error(error)
                main()

    #Buzzer
    if rec_cmd == 'buzzer':
        try:
            prp.buzz()
        except Exception as error:
            if tries > 0:
                report.report_error(error)
                main()
            else:
                report.report_error(f"To many tries: {error}")

    if rec_cmd[0:12] == 'buzzer_beep:':
        try:
            prp.beep(float(rec_cmd[12:]))
        except Exception as error:
            if tries > 0:
                report.report_error(error)
                main()
            else:
                report.report_error(f"To many tries: {error}")
