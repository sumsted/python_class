start_height = 60.0


def rocket_height(time):
    height = start_height + 2.31 * time ** 2 - 0.0013 * time ** 4 + 0.000034 * time ** 4.751
    return height


def launch_rocket():
    time = 0.0
    height = start_height

    while time <= 100.0:
        height = rocket_height(time)
        spaces = ' ' * (int(height) // 10)
        print('%6.2f seconds   %9.4f meters :%s*' % (time, height, spaces))
        if height < 50.0:
            time = time + 0.05
        else:
            time = time + 2.0


launch_rocket()