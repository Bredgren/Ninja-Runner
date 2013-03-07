import pygame
import funcs, game_vars, level, objects, data

def main():
    image = data.load_image("paused.png", 0)
    game_vars.screen.blit(image, (0,  0))
    pygame.display.flip()
    game_vars.screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_vars.runGame = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_vars.gameScreen = "intro"
                funcs.gameReset()
            if event.key == pygame.K_p:
                game_vars.gameScreen = "game"

