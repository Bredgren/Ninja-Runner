import math
import game_vars, funcs, objects, bullets, misc, data
from constants import *

class BaseEnemy:
    def checkDeath(self):
        pass

    def update(self):
        pass

class ball(BaseEnemy):
    def __init__(self, x, y):
        self.spriteFrameLeft1 = data.load_image('ball_left1.png')
        self.spriteFrameRight1 = data.load_image('ball_right1.png')
        
        self.spriteFrameLeft2 = data.load_image('ball_left2.png')
        self.spriteFrameRight2 = data.load_image('ball_right2.png')
        
        self.spriteFrameLeft3 = data.load_image('ball_left3.png')
        self.spriteFrameRight3 = data.load_image('ball_right3.png')
        self.sprite = self.spriteFrameRight1

        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()

        self.xPos = x
        self.yPos = y

        self.dir = 0
        self.speed = BALLSPEED

        self.walkTimer = 0
        self.walkTime = 3
        self.AnimDir = 0

        self.lives = BALL_LIVES
        self.damage = BALLDAMAGE
        self.canCollide = False

    def update(self):
        self.walkTimer += 1
        
        if self.dir == 1:
            self.xPos += self.speed

            if self.walkTimer > self.walkTime:
                if not (self.sprite == self.spriteFrameRight3 or
                        self.sprite == self.spriteFrameRight2 or
                        self.sprite == self.spriteFrameRight1):
                    self.sprite = self.spriteFrameRight1
                if self.sprite == self.spriteFrameRight1:
                    if self.AnimDir == 0:
                        self.sprite = self.spriteFrameRight3
                    else:
                        self.sprite = self.spriteFrameRight2
                elif self.sprite == self.spriteFrameRight2:
                    self.sprite = self.spriteFrameRight1
                    self.AnimDir = 0
                elif self.sprite == self.spriteFrameRight3:
                    self.sprite = self.spriteFrameRight1
                    self.AnimDir = 1
                self.walkTimer = 0

            for eachBlock in objects.blockList:
                if funcs.checkCollision(self, eachBlock):
                    while True:
                        if funcs.checkCollision(self, eachBlock):
                            self.xPos -= 1
                        else:
                            game_vars.ball_hit_wall.play()
                            self.dir = -1
                            self.sprite = self.spriteFrameLeft1
                            break
        else:
            self.xPos -= self.speed

            if self.walkTimer > self.walkTime:
                if not (self.sprite == self.spriteFrameLeft3 or
                        self.sprite == self.spriteFrameLeft2 or
                        self.sprite == self.spriteFrameLeft1):
                    self.sprite = self.spriteFrameLeft1
                if self.sprite == self.spriteFrameLeft1:
                    if self.AnimDir == 0:
                        self.sprite = self.spriteFrameLeft3
                    else:
                        self.sprite = self.spriteFrameLeft2
                elif self.sprite == self.spriteFrameLeft2:
                    self.sprite = self.spriteFrameLeft1
                    self.AnimDir = 0
                elif self.sprite == self.spriteFrameLeft3:
                    self.sprite = self.spriteFrameLeft1
                    self.AnimDir = 1
                self.walkTimer = 0

            for eachBlock in objects.blockList:
                if funcs.checkCollision(self, eachBlock):
                    while True:
                        if funcs.checkCollision(self, eachBlock):
                            self.xPos += 1
                        else:
                            game_vars.ball_hit_wall.play()
                            self.dir = 1
                            self.sprite = self.spriteFrameRight1
                            break

    def draw(self):
        game_vars.screen.blit(self.sprite, (self.xPos,  self.yPos))

class robot(BaseEnemy):
    def __init__(self, x, y):
        self.spriteFrameLeft1 = data.load_image('robot_left1.png')
        self.spriteFrameRight1 = data.load_image('robot_right1.png')
        
        self.spriteFrameLeft2 = data.load_image('robot_left2.png')
        self.spriteFrameRight2 = data.load_image('robot_right2.png')
        
        self.sprite = self.spriteFrameRight1

        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()

        self.xPos = x
        self.yPos = y

        self.dir = 0
        self.speed = ROBOTSPEED

        self.walkTimer = 0
        self.walkTime = 3

        self.lives = ROBOT_LIVES
        self.damage = ROBOTDAMAGE
        self.canCollide = False

    def update(self):
        self.walkTimer += 1
        
        if self.dir == 1:
            self.xPos += self.speed

            if self.walkTimer > self.walkTime:
                if not (self.sprite == self.spriteFrameRight2 or
                        self.sprite == self.spriteFrameRight1):
                    self.sprite = self.spriteFrameRight1
                if self.sprite == self.spriteFrameRight1:
                    self.sprite = self.spriteFrameRight2
                else:
                    self.sprite = self.spriteFrameRight1
                    
                self.walkTimer = 0

            for eachBlock in objects.blockList:
                if funcs.checkCollision(self, eachBlock):
                    while True:
                        if funcs.checkCollision(self, eachBlock):
                            self.xPos -= 1
                        else:
                            game_vars.robot_hit_wall.play()
                            self.dir = -1
                            self.sprite = self.spriteFrameLeft1
                            break
        else:
            self.xPos -= self.speed

            if self.walkTimer > self.walkTime:
                if not (self.sprite == self.spriteFrameLeft2 or
                        self.sprite == self.spriteFrameLeft1):
                    self.sprite = self.spriteFrameLeft1
                if self.sprite == self.spriteFrameLeft1:
                    self.sprite = self.spriteFrameLeft2
                else :
                    self.sprite = self.spriteFrameLeft1

                self.walkTimer = 0

            for eachBlock in objects.blockList:
                if funcs.checkCollision(self, eachBlock):
                    while True:
                        if funcs.checkCollision(self, eachBlock):
                            self.xPos += 1
                        else:
                            game_vars.robot_hit_wall.play()
                            self.dir = 1
                            self.sprite = self.spriteFrameRight1
                            break

    def draw(self):
        game_vars.screen.blit(self.sprite, (self.xPos,  self.yPos))

class spike(BaseEnemy):
    def __init__(self, x, y):
        self.sprite = data.load_image('floor_spike.png')
        self.xPos = x
        self.yPos = y
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.lives = -1
        self.canCollide = True
        self.damage = SPIKEDAMAGE

    def draw(self):
        game_vars.screen.blit(self.sprite, (self.xPos,  self.yPos))
        
