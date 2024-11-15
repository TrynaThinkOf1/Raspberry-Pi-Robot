from RpiL import Motor_Driver

driver = Motor_Driver(17, 27, 4, 5, 6, 13)

while True:
    cmd = input(">> ")

    if cmd == 'w':
        driver.forward()

    if cmd == 's':
        driver.backward()

    if cmd == 'a':
        driver.turn_left()

    if cmd == 'd':
        driver.turn_right()

    if cmd == 'c':
        driver.stop()