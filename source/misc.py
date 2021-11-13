import pygame, funcs, game_vars, objects, data
from constants import *

class decalHit:
    def __init__(self, sprite, xDir, yDir, time, x, y):
        if xDir < 0:
            self.sprite = data.load_image(sprite + '1.png')
        elif xDir > 0:
            self.sprite = data.load_image(sprite + '2.png')
        else:
            self.sprite = data.load_image(sprite)
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()

        self.xDir = xDir
        self.yDir = yDir

        self.xPos = x
        self.yPos = y

        self.lives = time

    def update(self):
        for block in objects.blockList:
            if funcs.checkCollision(self, block):
                if block.canCollide:
                    while funcs.checkCollision(self, block):
                        self.xPos += self.xDir
                        self.yPos += self.yDir

    def checkDeath(self):
        self.lives -= 1

        if self.lives == 0:
            return True

    def draw(self):
        game_vars.screen.blit(self.sprite, (self.xPos, self.yPos))

class energyBar:
    def __init__(self):
        self.topleft = (5, 15)
        self.width = 100
        self.height = 10
        self.textx = self.width // 2
        self.texty = (self.height // 2) + self.topleft[1]

    def update(self, value):
        self.width = value

    def draw(self):
        game_vars.screen.fill(DARKBLUE, (self.topleft[0], self.topleft[1], self.width, self.height))
        funcs.printText('Energy', 10, self.textx, self.texty, WHITE)
        
class healthBar:
    def __init__(self):
        self.topleft = (5, 5)
        self.width = 100
        self.height = 10
        self.textx = self.width // 2
        self.texty = (self.height // 2) + self.topleft[1]

    def update(self, value):
        self.width = value

    def draw(self):
        game_vars.screen.fill(GREEN, (self.topleft[0], self.topleft[1], self.width, self.height))
        funcs.printText('Health', 10, self.textx, self.texty, BLACK)
