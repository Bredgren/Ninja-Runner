import pygame
import game_vars, funcs, data, objects, misc
from constants import *

class basicBlock():
    def __init__(self, sprite, x, y):
        self.image = sprite
        self.sprite = data.load_image(self.image)
        self.xPos = x
        self.yPos = y
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.canCollide = True
        self.damage = 0

    def draw(self):
        game_vars.screen.blit(self.sprite, (self.xPos,  self.yPos))

class brokenBlock():
    def __init__(self, sprite, x, y):
        self.sprite = data.load_image(sprite)
        self.xPos = x
        self.yPos = y
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.bottom = (self.xPos+(self.width/2), self.yPos+self.height)
        self.canCollide = True
        self.damage = 0
        self.lives = 4

        self.falling = False
        self.delay = FALLDELAY
        self.time = 0

    def checkDeath(self):
        if self.falling:
            for eachBlock in objects.blockList:
                if funcs.checkCollision(self, eachBlock):
                    if (eachBlock.canCollide and eachBlock.xPos == self.xPos and
                        self.yPos >= eachBlock.yPos-BLOCKSIZE):
                        game_vars.block_hit.play()
                        objects.decalList.append(misc.decalHit("falling_block_hit.png", 0, -1, 1, self.xPos, self.yPos))
                        return True

    def update(self):
        if self.falling:
            self.time += 1
            if self.time >= self.delay:
                self.damage = FALLDAMAGE
                self.yPos += FALLSPEED



    def draw(self):
        game_vars.screen.blit(self.sprite, (self.xPos,  self.yPos))
