import pygame
import button, data, funcs
from constants import *

pygame.font.init()

blockList = []
bulletList = []
enemyList = []
decalList = []
health_battery = []
barList = []
mainButtonList = [
    button.textButton('Choose Level', 20, WIN_WIDTH // 2, (WIN_HEIGHT // 2) - 40),
    button.textButton('Instructions', 20, WIN_WIDTH // 2, (WIN_HEIGHT // 2)),
    button.textButton('Quit', 20, WIN_WIDTH // 2, (WIN_HEIGHT // 2) + 40),
]

lvl_names, times, player_pos, beatTimes = data.readFile('level data.txt')

levelButtonList = []
timeList = []
beatList = []
for level in range(len(lvl_names)):
    levelButtonList.append(button.textButton('%s' % lvl_names[level], 40, 0, -50))
    timeList.append(button.textButton('%s s' % float(times[level]), 30, 0, -50))
    beatList.append(button.textButton('%s s' % float(beatTimes[level]), 30, 0, -50))


pageButtonList = [
    button.textButton('<=', 30, 50, WIN_HEIGHT-50),
    button.textButton('main', 20, WIN_WIDTH/2, WIN_HEIGHT-50),
    button.textButton('=>', 30, WIN_WIDTH-50, WIN_HEIGHT-50),
]
    
characterButtonList = []

checkpoint = None
