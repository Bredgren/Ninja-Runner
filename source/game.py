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
    for block in objects.blockList:
        block.update()

    for block in objects.blockList:
        if block.checkDeath():
            objects.blockList.remove(block)

    for block in objects.blockList:
        block.draw()

    #---Update checkpoint---
    if objects.checkpoint:
        objects.checkpoint.update()
        objects.checkpoint.draw()

    #---Update Bullets---
    for bullet in objects.bulletList:
        for enemy in objects.enemyList:
            if funcs.checkCollision(bullet, enemy):
                objects.bulletList.remove(bullet)
                if not enemy.lives == -1:
                    if enemy.lives > 1:
                        enemy.lives -= 1
                    else:
                        if enemy.canCollide:
                            enemy.falling = True
                        else:
                            if enemy.damage == BALLDAMAGE:
                                game_vars.ball_death.play()
                            else:
                                game_vars.robot_death.play()
                            objects.enemyList.remove(enemy)

    for bullet in objects.bulletList:
        bullet.update()

    for bullet in objects.bulletList:
        if bullet.checkDeath():
            objects.bulletList.remove(bullet)

    for bullet in objects.bulletList:
        bullet.draw()

    #---Update Enemys---
    for enemy in objects.enemyList:
        enemy.update()

        if enemy.checkDeath():
            objects.enemyList.remove(enemy)

    for enemy in objects.enemyList:
        enemy.draw()

    #---Update Decals---
    for decal in objects.decalList:
        decal.update()

        if decal.checkDeath():
            objects.decalList.remove(decal)

        decal.draw()

    #---Update Healths and Batteriess---
    for item in objects.health_battery:
        item.update()
        item.draw()

    #---Update Player---
    objects.player.update()
    objects.player.draw()

    #---Change Screen---
    try:
        if objects.player.xPos + objects.player.width > WIN_WIDTH:
            funcs.changeLevel(level.levelSpawner.level[0] + 1, level.levelSpawner.level[1])
            objects.player.xPos = 0
        elif objects.player.xPos < 0:
            funcs.changeLevel(level.levelSpawner.level[0] - 1, level.levelSpawner.level[1])
            objects.player.xPos = WIN_WIDTH - objects.player.width
        elif objects.player.yPos + objects.player.height > WIN_HEIGHT:
            funcs.changeLevel(level.levelSpawner.level[0], level.levelSpawner.level[1] + 1)
            objects.player.yPos = 0
        elif objects.player.yPos < 0:
            funcs.changeLevel(level.levelSpawner.level[0], level.levelSpawner.level[1] - 1)
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
            elif event.key == pygame.K_p:
                game_vars.gameScreen = "paused"
            elif event.key == pygame.K_r:
                funcs.levelReset()

    # Show time and fps
    funcs.printText('%s s' %(round(game_vars.time / 1000.0, 2)), 20, 120, 10, BLACK, 1)
    funcs.printText('%s' %(round(game_vars.clock.get_fps(), 2)), 20, 5, WIN_HEIGHT - 15, LIGHTGREY, 1)

    #---Update Screen---
    pygame.display.flip()
