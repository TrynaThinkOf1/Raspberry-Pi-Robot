from RpiL import Motor_Driver

driver = Motor_Driver(17, 27, 4, 5, 6, 13)

funcs = {
    "w": driver.forward(),
    "s": driver.backward(),
    "d": driver.turn_right(),
    "a": driver.turn_left()
}

while True:
    cmd = input(">> ")

    if cmd in funcs:
        funcs[cmd]()