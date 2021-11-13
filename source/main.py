import pygame
import funcs, game_vars, game, level, finish, intro, pause, sys
from constants import *

def main():
    # Setup
    funcs.initGame(WIN_WIDTH, WIN_HEIGHT, game_vars.caption)

    # Main loop
    while game_vars.runGame:
        if game_vars.gameScreen == "game":
            if game_vars.firstCall:
                funcs.startGame()
                level.levelSpawner.draw()
                game_vars.firstCall = False
            game_vars.time += game_vars.clock.get_time()
            game.main()
        if game_vars.gameScreen == "intro":
            intro.main()
        if game_vars.gameScreen == "paused":
            pause.main()
        elif game_vars.gameScreen == "finish":
            finish.main()

        funcs.updateMusic()

        game_vars.clock.tick(game_vars.fpsLimit)

    pygame.quit()
    sys.exit()
