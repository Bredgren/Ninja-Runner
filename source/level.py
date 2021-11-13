import game_vars, funcs, blocks, objects, enemies, checkpoint, powerups, data, player
from constants import *

levelSpawner = None
background = None

class LevelSpawner:
    def __init__(self):
        self.sprite = data.load_image(game_vars.levelName)
        self.level = game_vars.startLevel

    def reset(self):
        if game_vars.levelName:
            self.sprite = data.load_image(game_vars.levelName)
        self.level = game_vars.startLevel

    def draw(self):
        for xPixel in range(LVLWIDTH + 2):
            xPixel -= 1
            for yPixel in range(LVLHEIGHT + 2):
                yPixel -= 1

                color = self.sprite.get_at((int(xPixel + (self.level[0] * LVLWIDTH)),
                                            int(yPixel + (self.level[1] * LVLHEIGHT))))

                xPos = xPixel * BLOCKSIZE
                yPos = yPixel * BLOCKSIZE

                if color == ITEMDICT['grey floor']:
                    objects.blockList.append(blocks.basicBlock('grey_block.png', xPos, yPos))
                elif color == ITEMDICT['metal floor']:
                    objects.blockList.append(blocks.basicBlock('metal_floor.png', xPos, yPos))
                elif color == ITEMDICT['metal solid']:
                    objects.blockList.append(blocks.basicBlock('metal_wall_solid.png', xPos, yPos))
                elif color == ITEMDICT['metal wallL']:
                    objects.blockList.append(blocks.basicBlock('metal_wallL.png', xPos, yPos))
                elif color == ITEMDICT['metal wallR']:
                    objects.blockList.append(blocks.basicBlock('metal_wallR.png', xPos, yPos))
                elif color == ITEMDICT['metal cornerBL']:
                    objects.blockList.append(blocks.basicBlock('metal_cornerBL.png', xPos, yPos))
                elif color == ITEMDICT['metal cornerBR']:
                    objects.blockList.append(blocks.basicBlock('metal_cornerBR.png', xPos, yPos))
                elif color == ITEMDICT['metal cornerTL']:
                    objects.blockList.append(blocks.basicBlock('metal_cornerTL.png', xPos, yPos))
                elif color == ITEMDICT['metal cornerTR']:
                    objects.blockList.append(blocks.basicBlock('metal_cornerTR.png', xPos, yPos))
                elif color == ITEMDICT['door']:
                    objects.blockList.append(blocks.basicBlock('lock_door.png', xPos, yPos))
                elif color == ITEMDICT['door top']:
                    objects.blockList.append(blocks.basicBlock('lock_door_top.png', xPos, yPos))
                elif color == ITEMDICT['light']:
                    objects.blockList.append(blocks.basicBlock('light.png', xPos, yPos))
                elif color == ITEMDICT['white cealing']:
                    objects.blockList.append(blocks.basicBlock('white_cealing.png', xPos, yPos))
                elif color == ITEMDICT['broken floor']:
                    objects.enemyList.append(blocks.brokenBlock('cracked_metal_floor.png',xPos, yPos))
                elif color == ITEMDICT['broken solid']:
                    objects.enemyList.append(blocks.brokenBlock('broken_solid.png',xPos, yPos))

                elif color == ITEMDICT['checkpoint']:
                    objects.checkpoint = checkpoint.checkpoint(xPos, yPos)
                    
                elif color == ITEMDICT['jet pack']:
                    objects.decalList.append(powerups.jetPack(xPos + 2, yPos))
                elif color == ITEMDICT['teleport']:
                    objects.decalList.append(powerups.teleport(xPos + 2, yPos + 2))
                
                elif color == ITEMDICT['health']:
                    objects.health_battery.append(powerups.health(xPos, yPos))
                elif color == ITEMDICT['battery']:
                    objects.health_battery.append(powerups.battery(xPos, yPos))
                        
                elif color == ITEMDICT['ball enemy']:
                    objects.enemyList.append(enemies.ball(xPos, yPos))
                elif color == ITEMDICT['robot enemy']:
                    objects.enemyList.append(enemies.robot(xPos, yPos))
                elif color == ITEMDICT['floor spike']:
                    objects.enemyList.append(enemies.spike(xPos, yPos))

class Background:
    def __init__(self):
        self.sprite = data.load_image('lightBlueBgd.png', 0)

    def draw(self):
        game_vars.screen.blit(self.sprite, (0,  0))
