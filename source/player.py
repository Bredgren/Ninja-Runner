import pygame
import funcs, game_vars, objects, bullets, data
from constants import *
from pygame.locals import *

class player():
    def __init__(self, x, y):
        self.spriteFrameLeft1 = data.load_image('ninja_stillL.png')
        self.spriteFrameRight1 = data.load_image('ninja_stillR.png')
        
        self.spriteFrameLeft2 = data.load_image('ninja_run1L.png')
        self.spriteFrameRight2 = data.load_image('ninja_run1R.png')
        
        self.spriteFrameLeft3 = data.load_image('ninja_run2L.png')
        self.spriteFrameRight3 = data.load_image('ninja_run2R.png')

        self.spriteFrameLeft4 = data.load_image('ninja_attackL.png')
        self.spriteFrameRight4 = data.load_image('ninja_attackR.png')

        self.spriteFrameLeft5 = data.load_image('ninja_jumpL.png')
        self.spriteFrameRight5 = data.load_image('ninja_jumpR.png')

        self.sprite = self.spriteFrameLeft1

        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()

        self.xPos = x
        self.yPos = y

        self.dir = 1

        self.yVel = 0.0

        self.jumped = False
        self.teleported = False

        self.energy = 100
        self.health = 100

        self.reloadTimer = 0
        self.reloadTime = RELOAD_TIME

        self.walkTimer = 0
        self.walkTime = 3

    def dead(self):
        if self.health <= 0:
            return True
        else:
            return False

    def update(self):
        self.movment()

        if self.reloadTimer > 0:
            self.reloadTimer -= 1
        else:
            if funcs.keyPressed(K_SPACE):
                game_vars.throw.play()
                objects.bulletList.append(bullets.basicBullet((self.xPos), (self.yPos + 6), self.dir))
                if self.dir == 1:
                    self.sprite = self.spriteFrameRight4
                else:
                    self.sprite = self.spriteFrameLeft4
                self.reloadTimer = self.reloadTime

        for eachEnemy in objects.enemyList:
            if funcs.checkCollision(self, eachEnemy):
                self.health -= eachEnemy.damage

        objects.energyBar.update(self.energy)
        if self.health > 100:
            self.health = 100
        objects.healthBar.update(self.health)

        if self.dead():
            self.xPos = game_vars.saveXPos
            self.yPos = game_vars.saveYPos
            funcs.changeLevel(game_vars.saveLevel[0],game_vars.saveLevel[1])
            self.health = 100
            self.energy = 100


    def movment(self):

        if not self.jumped:
            if self.dir == 1:
                self.sprite = self.spriteFrameRight1
            else:
                self.sprite = self.spriteFrameLeft1

        #---------Teleport
        for event in game_vars.events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if game_vars.powerTeleport and self.energy >= 75:
                        game_vars.teleport.play()
                        self.xPos = event.pos[0] - self.width/2
                        self.yPos = event.pos[1] - self.height/2
                        self.energy -= 75
                        self.teleported = True

        #---------X movment
        if funcs.keyPressed(K_d)or funcs.keyPressed(K_RIGHT):
            if not (self.sprite == self.spriteFrameRight2 or
                    self.sprite == self.spriteFrameRight3):
                self.sprite = self.spriteFrameRight2
            self.dir = 1
            self.xPos += PLAYERSPEED
            self.walkTimer += 1
            if self.walkTimer > self.walkTime:
                if self.sprite == self.spriteFrameRight3:
                    self.sprite = self.spriteFrameRight2
                else:
                    self.sprite = self.spriteFrameRight3
                self.walkTimer = 0
                
            if self.energy < 100:
                self.energy += 0.1


            for eachBlock in objects.blockList:
                if funcs.checkCollision(self, eachBlock):
                    if 'door' in eachBlock.image:
                        game_vars.gameScreen = 'finish'
                    if eachBlock.canCollide:
                        while funcs.checkCollision(self, eachBlock):
                            self.xPos -= 1

        elif funcs.keyPressed(K_a) or funcs.keyPressed(K_LEFT):
            if not (self.sprite == self.spriteFrameLeft2 or
                    self.sprite == self.spriteFrameLeft3):
                self.sprite = self.spriteFrameLeft2
            self.dir = -1
            self.xPos -= PLAYERSPEED
            self.walkTimer += 1
            if self.walkTimer > self.walkTime:
                if self.sprite == self.spriteFrameLeft3:
                    self.sprite = self.spriteFrameLeft2
                else:
                    self.sprite = self.spriteFrameLeft3
                self.walkTimer = 0

            for eachBlock in objects.blockList:
                if funcs.checkCollision(self, eachBlock):
                    if 'door' in eachBlock.image:
                        game_vars.gameScreen = 'finish'
                    if eachBlock.canCollide:
                        while funcs.checkCollision(self, eachBlock):
                            self.xPos += 1
         
            if self.energy < 100:
                self.energy += 0.1
        else:
            if self.jumped:
                if self.dir == 1:
                    self.sprite = self.spriteFrameRight5
                else:
                    self.sprite = self.spriteFrameLeft5

        if self.teleported:
            if self.dir == 1:
                self.sprite = self.spriteFrameRight5
            else:
                self.sprite = self.spriteFrameLeft5
            self.teleported = False


        #-------Y movment

        for event in game_vars.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    if not self.jumped:
                        if self.dir == 1:
                            self.sprite = self.spriteFrameRight5
                        else:
                            self.sprite = self.spriteFrameLeft5
                        self.yVel = JUMP_FORCE
                        self.jumped = True
                        
                    if self.energy < 100:
                        self.energy += 1
                        
        if funcs.keyPressed(K_s) or funcs.keyPressed(K_DOWN):
            if game_vars.powerJetPack and self.energy >= 5:
                self.yVel += FLY_FORCE
                self.energy -= 2
                if self.dir ==1:
                    self.sprite = self.spriteFrameRight5
                else:
                    self.sprite = self.spriteFrameLeft5


        if self.yVel != 0 and self.jumped == False:
            self.jumped = True

        self.yPos -= self.yVel

        if self.yVel > -10:
            self.yVel -= GRAVITY


        if self.yVel >= 1:

            for eachBlock in objects.blockList:
                if funcs.checkCollision(self, eachBlock):
                    if eachBlock.canCollide:
                        while True:
                            if funcs.checkCollision(self, eachBlock):
                                self.yPos += 1
                            else:
                                self.yVel = 0
                                break
            for eachEnemy in objects.enemyList:
                if funcs.checkCollision(self, eachEnemy):
                    if eachEnemy.canCollide:
                        eachEnemy.falling = True
                        self.health -= eachEnemy.damage
                        while True:
                            if funcs.checkCollision(self, eachEnemy):
                                self.yPos += 1
                            else:
                                self.yVel = 0
                                break

        else:

            for eachBlock in objects.blockList:
                if funcs.checkCollision(self, eachBlock):
                    if eachBlock.canCollide:
                        while True:
                            if funcs.checkCollision(self, eachBlock):
                                self.yPos -= 1
                            else:
                                self.jumped = False
                                self.yVel = 0
                                break
            for eachEnemy in objects.enemyList:
                if funcs.checkCollision(self, eachEnemy):
                    if eachEnemy.canCollide:
                        eachEnemy.falling = True
                        self.health -= eachEnemy.damage
                        while True:
                            if funcs.checkCollision(self, eachEnemy):
                                self.yPos -= 1
                            else:
                                self.jumped = False
                                self.yVel = 0
                                break


    def draw(self):
        game_vars.screen.blit(self.sprite, (self.xPos,  self.yPos))




