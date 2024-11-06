import requests
import time

command_list_help = {
    "fwd:(centimeters)": "Robot moves forward the amount of centimeters inputted",
    "bkd:(centimeters)": "Robot moves backward the amount of centimeters inputted",
    "left:(degrees)": "Robot turns left the amount of degrees inputted",
    "right:(degrees)": "Robot turns right the amount of degrees inputted",
    "red_LED": "Built in Red LED turns on",
    "white_LED": "Built in White LED turns on",
    "buzzer": "Built in Piezo buzzer starts buzzing",
    "buzzer_beep:(seconds)": "Built in Piezo buzzer beeps 8 times with an interval of seconds inputted"
}

command_list_valid = [
    "fwd:", "bkd:", "left:", "right:", "red_LED", "white_LED", "buzzer", "buzzer_beep:"
]

def main():
    while True:
        get_command()


def get_command():
        command = str(input(">> "))
        #system command checks
        if command.upper() == 'HELP':
            for command in command_list_help:
                print(command + " -> " + command_list_help[command] + "\n")
        elif command.upper() == 'ERRORS':
            try:
                print(requests.get("http://localhost:5000/see_errors").content.decode('utf-8'))
            except Exception as e:
                print(e)
                print("\n" * 5)
                main()
        elif command.upper() == 'UPDATES':
            try:
                print(requests.get("http://localhost:5000/see_updates").content.decode('utf-8'))
            except Exception as e:
                print(e)
                print("\n" * 5)
                main()
        elif command.upper() == 'CLEAR':
            try:
                print("\n" * 50)
            except Exception as e:
                print(e)
                print("\n" * 5)
                main()

        #robot command check
        elif command[0:4] in command_list_valid:
            try:
                requests.get("http://localhost:5000/give_command", params={"command":command})
                time.sleep(0.15)
                print("    " + requests.get("http://localhost:5000/see_app_update").content.decode('utf-8') + "\n")
                time.sleep(0.15)
                print("    " + requests.get("http://localhost:5000/see_app_update").content.decode('utf-8') + "\n")
            except Exception as e:
                print(e)
                print("\n" * 5)
                main()
        else:
            print("Invalid command")

if __name__ == "__main__":
    print("'Help' for help, 'Errors' for errors, 'Updates' for full updates, 'Clear' to clear screen")
    main()
