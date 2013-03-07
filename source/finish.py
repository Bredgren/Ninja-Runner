import pygame
import game_vars, data, funcs, objects
from constants import *

def main():
    image = data.load_image("finish.png", 0)
    game_vars.screen.blit(image, (0,  0))

    time = round(game_vars.time/1000.0,2)
    funcs.printText('Your time was %s s' %(time), 20, WIN_WIDTH/2, (WIN_HEIGHT/2)-30, BLACK)

    if time > float(objects.times[game_vars.levelIndex]):
        funcs.printText('You did not beat the time of %s s'
                        %(objects.times[game_vars.levelIndex]), 20, WIN_WIDTH/2, (WIN_HEIGHT/2), BLACK)
    else:
        funcs.printText('New Record!', 30, WIN_WIDTH/2, (WIN_HEIGHT/2), BLACK)
        objects.times[game_vars.levelIndex] = round(float(time),2)
        data.writeFile('level data.txt', objects.lvl_names, objects.times, objects.player_pos, objects.beatTimes)
        
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_vars.runGame = False
        elif event.type == pygame.KEYDOWN:
            game_vars.gameScreen = "intro"
            funcs.gameReset()
            
