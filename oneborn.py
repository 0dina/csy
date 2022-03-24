import time

from adafruit_motorkit import MotorKit
kit = MotorKit()

throttle = 0.0

while True:
    print('speed up')
    for i in range(100):
        throttle = i/100
        print('throttle: ', throttle)
        kit.motor1.throttle = throttle
        time.sleep(0.01)

    print('speed down')
    for i in range(100):
        throttle = 1 - i/100
        print('throttle: ', throttle)
        kit.motor1.throttle = throttle
        time.sleep(0.01)
