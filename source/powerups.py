import game_vars, funcs, objects, data
from constants import *

class BasePowerUp:
    def checkDeath(self):
        pass

class teleport(BasePowerUp):
    def __init__(self, x, y):
        self.sprite = data.load_image('teleport.png')
        self.xPos = x
        self.yPos = y
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()

    def update(self):
        if funcs.checkCollision(self, objects.player) and not game_vars.powerTeleport:
            game_vars.powerTeleport = True
            
    def draw(self):
        if not game_vars.powerTeleport:
            game_vars.screen.blit(self.sprite, (self.xPos, self.yPos))
        else:
            funcs.printText('T', 10, 25, 33, BLACK)

class jetPack(BasePowerUp):
    def __init__(self, x, y):
        self.sprite = data.load_image('jet_pack.png')
        self.xPos = x
        self.yPos = y
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()

    def update(self):
        if funcs.checkCollision(self, objects.player) and not game_vars.powerJetPack:
            game_vars.jet_pack.play()
            game_vars.powerJetPack = True
            
    def draw(self):
        if not game_vars.powerJetPack:
            game_vars.screen.blit(self.sprite, (self.xPos, self.yPos))
        else:
            funcs.printText('J', 10, 10, 33, BLACK)

class health(BasePowerUp):
    def __init__(self, x, y):
        self.sprite = data.load_image('health.png')
        self.xPos = x
        self.yPos = y
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.used = False

    def update(self):
        if funcs.checkCollision(self, objects.player) and not self.used:
            game_vars.heal.play()
            self.used = True
            objects.player.health += 50

    def draw(self):
        if not self.used:
            game_vars.screen.blit(self.sprite, (self.xPos, self.yPos))

class battery(BasePowerUp):
    def __init__(self, x, y):
        self.sprite = data.load_image('battery.png')
        self.xPos = x
        self.yPos = y
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.used = False

    def update(self):
        if funcs.checkCollision(self, objects.player) and not self.used:
            game_vars.battery_pickup.play()
            self.used = True
            objects.player.energy = 100

    def draw(self):
        if not self.used:
            game_vars.screen.blit(self.sprite, (self.xPos, self.yPos))
