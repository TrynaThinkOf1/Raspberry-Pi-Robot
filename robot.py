from RpiL import Motor_Driver

driver = Motor_Driver(17, 27, 4, 5, 6, 13)

while True:
    cmd = input(">> ")

    if cmd == 'w':
        try:
            driver.forward()
        except Exception as e:
            print(e)
            continue

    elif cmd == 'a':
        try:
            driver.turn_left()
        except Exception as e:
            print(e)
            continue

    elif cmd == 'd':
        try:
            driver.turn_right()
        except Exception as e:
            print(e)
            continue

    elif cmd == 's':
        try:
            driver.backward()
        except Exception as e:
            print(e)
            continue

    elif cmd == 'c':
        try:
            driver.stop()
        except Exception as e:
            print(e)
            continue