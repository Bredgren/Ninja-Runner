import pygame
import game_vars, objects, level, funcs, checkpoint
from constants import *

def main():

    #---Reset Screen and Draw Background
    game_vars.screen.fill((0,0,0))

    level.background.draw()

    #---Get events---
    game_vars.events = pygame.event.get()

    #---Update Blocks---
    for eachBlock in  objects.blockList:
        try:
            eachBlock.update()
        except:
            pass

    for eachBlock in  objects.blockList:
        try:
            if eachBlock.checkDeath():
                objects.blockList.remove(eachBlock)
        except:
            pass

    for eachBlock in  objects.blockList:
        eachBlock.draw()

    #---Update checkpoint---
    try:
        objects.checkpoint.update()
        objects.checkpoint.draw()
    except:
        pass

    #---Update Bullets---
    for eachBullet in objects.bulletList:
        for eachEnemy in objects.enemyList:
            if funcs.checkCollision(eachBullet, eachEnemy):
                try: objects.bulletList.remove(eachBullet)
                except: pass
                if not eachEnemy.lives == -1:
                    if eachEnemy.lives > 1:
                        eachEnemy.lives -= 1
                    else:
                        if eachEnemy.canCollide:
                            eachEnemy.falling = True
                        else:
                            if eachEnemy.damage == BALLDAMAGE:
                                game_vars.ball_death.play()
                            else:
                                game_vars.robot_death.play()
                            objects.enemyList.remove(eachEnemy)


    for eachBullet in objects.bulletList:
        eachBullet.update()

    for eachBullet in objects.bulletList:
        if eachBullet.checkDeath():
            try: objects.bulletList.remove(eachBullet)
            except: pass


    for eachBullet in objects.bulletList:
        eachBullet.draw()

    #---Update Enemys---
    for eachEnemy in objects.enemyList:
        try: eachEnemy.update()
        except: pass

        try:
            if eachEnemy.checkDeath():
                objects.enemyList.remove(eachEnemy)

        except:
            pass
    for eachEnemy in objects.enemyList:
        eachEnemy.draw()

    #---Update Decals---
    for eachDecal in  objects.decalList:
        try:
            eachDecal.update()
        except:
            pass

        try:
            if eachDecal.checkDeath():
                objects.decalList.remove(eachDecal)
        except:
            pass

        eachDecal.draw()

    #---Update Healths and Batteriess---
    for item in objects.health_battery:
        try:
            item.update()
        except:
            pass
        item.draw()


    #---Update Player---
    objects.player.update()
    objects.player.draw()

    #---Change Screen---
    try:
        if objects.player.xPos + objects.player.width > WIN_WIDTH:
            funcs.changeLevel(level.levelSpawner.level[0]+1, level.levelSpawner.level[1])
            objects.player.xPos = 0
        elif objects.player.xPos < 0:
            funcs.changeLevel(level.levelSpawner.level[0]-1, level.levelSpawner.level[1])
            objects.player.xPos = WIN_WIDTH - objects.player.width
        elif objects.player.yPos + objects.player.height > WIN_HEIGHT:
            funcs.changeLevel(level.levelSpawner.level[0], level.levelSpawner.level[1]+1)
            objects.player.yPos = 0
        elif objects.player.yPos < 0:
            funcs.changeLevel(level.levelSpawner.level[0], level.levelSpawner.level[1]-1)
            objects.player.yPos = WIN_HEIGHT - objects.player.height
    except IndexError:
        level.levelSpawner.level = game_vars.startLevel
        objects.player.health = 0

    #---Update Bars-------
    objects.energyBar.draw()
    objects.healthBar.draw()
    if game_vars.powerJetPack:
        funcs.printText('J', 10, 10, 33, BLACK)
    if game_vars.powerTeleport:
        funcs.printText('T', 10, 25, 33, BLACK)

    #---Check if closed---
    for event in game_vars.events:
        if event.type == pygame.QUIT:
            game_vars.runGame = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                funcs.gameReset()
            if event.key == pygame.K_p:
                game_vars.gameScreen = "paused"

    # Show time and fps
    funcs.printText('%s s' %(round(game_vars.time/1000.0,2)), 20, 120, 10, BLACK, 1)
    funcs.printText('%s' %(round(game_vars.clock.get_fps(),2)), 20, 5, WIN_HEIGHT-15, LIGHTGREY, 1)


    #---Update Screen---
    pygame.display.flip()
