import robot_controller


class Robot:
    def __init__(self, name, debug):
        self.name = name
        robot_controller.robot_debug = debug
        print(self.name, 'robot is online')

    def forward(self):
        print(self.name, 'robot is moving forward')
        robot_controller.forward()

    def backward(self):
        print(self.name, 'robot is moving backward')
        robot_controller.backward()

    def left(self):
        print(self.name, 'robot is moving left')
        robot_controller.left()

    def right(self):
        print(self.name, 'robot is moving right')
        robot_controller.right()

    def distance(self):
        print(self.name, 'robot distance')
        robot_controller.distance()

    def blink(self, times):
        print(self.name, 'robot is blinking')
        robot_controller.blink(times)


if __name__ == '__main__':

    my_robot = Robot('MattBot', True)


    for i in range(5):
        my_robot.forward()

    my_robot.left()

    for i in range(3):
        my_robot.forward()

    my_robot.right()

    for i in range(3):
        my_robot.forward()

    my_robot.right()

    for i in range(8):
        my_robot.forward()

    my_robot.distance()
    my_robot.blink(10)
