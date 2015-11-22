import socket
import server
from mcpi import block
from mcpi import minecraft
import shapes
from woolcolors import WoolColors


class SimpleMine:
    COLORS = {
        'y': WoolColors.yellow,
        'x': WoolColors.black,
        'g': WoolColors.green,
        'G': WoolColors.dark_green,
        'b': WoolColors.blue,
        'p': WoolColors.purple,
        'r': WoolColors.red,
        'P': WoolColors.pink,
        'o': WoolColors.orange,
        'B': WoolColors.brown,
        'e': WoolColors.light_gray
    }

    def __init__(self, name):
        self.name = name
        self.mc = minecraft.Minecraft.create(server.address)
        self.ip = socket.getfqdn()

    def reset_world(self):
        self.mc.setBlocks(-30, 0, -15, 30, 60, 42, block.AIR)
        self.mc.player.setPos(0, 0, 0)
        self.chat('World reset by ' + self.ip)

    def make_thing(self, thing, depth=1):
        pos = self.mc.player.getPos()
        pos = minecraft.Vec3(int(pos.x), int(pos.y), int(pos.z))
        for x_delta in range(depth):
            height = len(thing)
            for row in thing:
                idx = 0
                for b in row:
                    if b != ' ':
                        self.mc.setBlock(pos.x + x_delta + 1, pos.y + height, pos.z + idx, block.WOOL.id,
                                         SimpleMine.COLORS[b].value)
                    idx += 1
                height -= 1
        self.chat('Thing made by ' + self.name)

    def chat(self, message):
        self.mc.postToChat(message)


if __name__ == '__main__':
    steve = SimpleMine('Steve')
    steve.make_thing(shapes.santa)

    # steve.reset_world()
    # sm.build_tower()
    # sm.mc.player.setPos((0,0,0))
    # pos = sm.mc.player.getPos()
    # print(str(pos))
