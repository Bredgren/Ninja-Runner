import pygame
import game_vars, funcs, level, objects, data
from constants import *

# TODO: display "+1000np" when all ninja times beaten

def main():
    if game_vars.introScreen == "main":
        game_vars.screen.fill(BLACK)
        image = data.load_image("intro.png")
        game_vars.screen.blit(image, (0,  0))

        mousePos = pygame.mouse.get_pos()
        for button in objects.mainButtonList:
            button.update(mousePos)
            button.draw()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in objects.mainButtonList:
                        if button.selected:
                            if button.message == 'Choose Level':
                                game_vars.introScreen = "choose level"
                            elif button.message == 'Instructions':
                                game_vars.introScreen = "instructions"
                            elif button.message == 'Quit':
                                game_vars.runGame = False
            elif event.type == pygame.QUIT:
                game_vars.runGame = False
        
        pygame.display.flip()
        
    elif game_vars.introScreen == "choose level":
        image = data.load_image('choose_level.png')
        game_vars.screen.blit(image, (0,0))
        pages = int(len(objects.levelButtonList)/7) + 1
        firstItem = (6 * game_vars.lvlPage) - 6
        lastItem = (game_vars.lvlPage * 6)
        try:
            objects.levelButtonList[lastItem-1]
        except:
            lastItem = None

        mousePos = pygame.mouse.get_pos()

        for lvl in range(len(objects.levelButtonList[firstItem:lastItem])):
            dispLoc = (20 + (objects.levelButtonList[lvl+firstItem].rect.width/2),
                       130 + (70 * lvl))
            objects.levelButtonList[lvl+firstItem].xPos = dispLoc[0]
            objects.levelButtonList[lvl+firstItem].yPos = dispLoc[1]
            objects.levelButtonList[lvl+firstItem].update(mousePos)
            objects.levelButtonList[lvl+firstItem].draw()

            timeDispLoc = ((WIN_WIDTH-(objects.timeList[lvl+firstItem].rect.width/2))-150,
                            130 + (70 * lvl))
            objects.timeList[lvl+firstItem].xPos = timeDispLoc[0]
            objects.timeList[lvl+firstItem].yPos = timeDispLoc[1]
            objects.timeList[lvl+firstItem].update(mousePos)
            objects.timeList[lvl+firstItem].size = objects.timeList[lvl+firstItem].initSize
            if float(objects.times[lvl+firstItem]) <= float(objects.beatTimes[lvl+firstItem]):
                objects.timeList[lvl+firstItem].color = GREEN
            objects.timeList[lvl+firstItem].draw()

            beatDispLoc = ((WIN_WIDTH-(objects.timeList[lvl+firstItem].rect.width/2))-10,
                            130 + (70 * lvl))
            objects.beatList[lvl+firstItem].xPos = beatDispLoc[0]
            objects.beatList[lvl+firstItem].yPos = beatDispLoc[1]
            objects.beatList[lvl+firstItem].update(mousePos)
            objects.beatList[lvl+firstItem].size = objects.beatList[lvl+firstItem].initSize
            objects.beatList[lvl+firstItem].draw()

        objects.pageButtonList[2].update(mousePos)
        objects.pageButtonList[0].update(mousePos)
        objects.pageButtonList[1].update(mousePos)
        
        if game_vars.lvlPage < pages:
            objects.pageButtonList[2].draw()
        if game_vars.lvlPage > 1:
            objects.pageButtonList[0].draw()  
        objects.pageButtonList[1].draw()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in objects.pageButtonList:
                        if button.selected:
                            if button.message == '=>' and game_vars.lvlPage < pages:
                                game_vars.lvlPage += 1
                            elif button.message == '<=' and game_vars.lvlPage > 1:
                                game_vars.lvlPage -= 1
                            elif button.message == 'main':
                                game_vars.introScreen = "main"
                                game_vars.lvlPage = 1
                    for button in objects.levelButtonList[firstItem:lastItem]:
                        if button.selected:
                            game_vars.levelName = button.message + '.png'
                            game_vars.gameScreen = "game"
                            game_vars.levelIndex = objects.levelButtonList.index(button)
                            game_vars.saveLevel = objects.player_pos[game_vars.levelIndex]
                            game_vars.startLevel = objects.player_pos[game_vars.levelIndex]
                            try:
                                level.levelSpawner.reset()
                            except: pass 
            elif event.type == pygame.QUIT:
                game_vars.runGame = False

        pygame.display.flip()

    elif game_vars.introScreen == 'instructions':
        image = data.load_image('instructions.png')
        game_vars.screen.blit(image, (0,0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_vars.runGame = False
            elif event.type == pygame.KEYDOWN:
                game_vars.introScreen = "main"
