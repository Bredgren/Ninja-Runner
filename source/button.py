import pygame
import game_vars, sys
from constants import *

class textButton:
    def __init__(self, text, size, x, y):
        self.message = text
        self.initSize = size
        self.size = self.initSize
        self.xPos = x
        self.yPos = y
        self.selected = False
        self.color = BLACK
        self.rect = getText(self.message, self.size, self.xPos, self.yPos, self.color).get_rect()

    def update(self, mousePos):
        if (mousePos[0] > self.rect.left and mousePos[0] < self.rect.right and
            mousePos[1] > self.rect.top and mousePos[1] < self.rect.bottom):
            self.selected = True
        else:
            self.selected = False

        if self.selected:
            self.size = self.initSize * 2
        else:
            self.size = self.initSize

    def draw(self):
        text = getText(self.message, self.size, self.xPos, self.yPos, self.color)
        self.rect = text.get_rect(centerx = self.xPos, centery = self.yPos)
        
        game_vars.screen.blit(text, self.rect)

def getText(text, size, x, y, color):
    font = pygame.font.SysFont('arial', size)
    return font.render((str(text)), 1, color)
