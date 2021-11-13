import funcs, game_vars, objects, level, data

class checkpoint:
    def __init__(self, x, y):
        self.sprite1 = data.load_image("checkpoint1.png")
        self.sprite2 = data.load_image("checkpoint2.png")
        self.sprite = self.sprite1

        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        
        self.xPos = x
        self.yPos = y

    def update(self):
        if game_vars.saveLevel == level.levelSpawner.level and self.xPos == game_vars.saveXPos and self.yPos == game_vars.saveYPos:
            self.sprite = self.sprite2
        else:
            self.sprite = self.sprite1
            if funcs.checkCollision(self, objects.player):
                game_vars.check.play()
                game_vars.saveLevel = level.levelSpawner.level
                game_vars.saveXPos = self.xPos
                game_vars.saveYPos = self.yPos

    def draw(self):
        game_vars.screen.blit(self.sprite, (self.xPos, self.yPos))
