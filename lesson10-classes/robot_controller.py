import time

import gopigo_client

robot_debug = True
robot_wait = .5
robot_speed = 100


def forward():
    print('robot_controller, forward, robot_debug =', robot_debug)
    if not robot_debug:
        gopigo_client.set_speed(robot_speed)
        gopigo_client.stop()
        gopigo_client.fwd()
        time.sleep(robot_wait)
        gopigo_client.stop()


def backward():
    print('robot_controller, right, robot_debug =', robot_debug)
    if not robot_debug:
        gopigo_client.set_speed(robot_speed)
        gopigo_client.stop()
        gopigo_client.bwd()
        time.sleep(robot_wait)
        gopigo_client.stop()


def left():
    print('robot_controller, left, robot_debug =', robot_debug)
    if not robot_debug:
        gopigo_client.set_speed(robot_speed)
        gopigo_client.stop()
        gopigo_client.left_rot()
        time.sleep(robot_wait)
        gopigo_client.stop()


def right():
    print('robot_controller, right, robot_debug =', robot_debug)
    if not robot_debug:
        gopigo_client.set_speed(robot_speed)
        gopigo_client.stop()
        gopigo_client.right_rot()
        time.sleep(robot_wait)
        gopigo_client.stop()


def stop():
    print('robot_controller, stop, robot_debug =', robot_debug)
    if not robot_debug:
        gopigo_client.set_speed(robot_speed)
        gopigo_client.stop()


def distance():
    print('robot_controller, distance, robot_debug =', robot_debug)
    if not robot_debug:
        d = gopigo_client.us_dist(0)
        print('robot_controller, distance =', d)


def blink(times=5):
    times = times if times < 10 else 5
    print('robot_controller, blink, robot_debug =', robot_debug)
    if not robot_debug:
        for i in range(times):
            gopigo_client.led_on(0)
            gopigo_client.led_on(1)
            gopigo_client.led_off(0)
            gopigo_client.led_off(1)


if __name__ == '__main__':
    robot_debug = False
    left()
    right()
    forward()
    forward()
    distance()

