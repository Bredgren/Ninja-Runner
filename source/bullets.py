import game_vars, funcs, objects, misc, data
from constants import *

class basicBullet:
    def __init__(self, x, y, direction):
        self.sprite = data.load_image("star.png")

        self.xPos = x
        self.yPos = y
        self.height = self.sprite.get_height()
        self.width = self.sprite.get_width()

        self.dir = direction # -1 or 1
        self.speed = BULLETSPEED

    def update(self):
        self.xPos += (self.dir * self.speed)

    def checkDeath(self):
        if self.xPos > WIN_WIDTH + self.width or self.xPos < 0 or self.yPos > WIN_HEIGHT + self.height or self. yPos <  0:
            return True
        else:
            for eachBlock in objects.blockList:
                if funcs.checkCollision(self, eachBlock):
                    return True

        return False

    def draw(self):
        game_vars.screen.blit(self.sprite, (self.xPos, self.yPos))
