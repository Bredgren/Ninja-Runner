import game_vars, funcs, blocks, objects, enemies, checkpoint, powerups, data, player
from constants import *

class levelSpawner():
    def __init__(self):
        self.sprite = data.load_image(game_vars.levelName)
        self.level = game_vars.startLevel

    def reset(self):
        self.sprite = data.load_image(game_vars.levelName)
        self.level = game_vars.startLevel

    def draw(self):

        for xPixel in range(LVLWIDTH+2):
            xPixel -= 1
            for yPixel in range(LVLHEIGHT+2):
                yPixel -= 1

                if self.sprite.get_at((int(xPixel + (self.level[0] * LVLWIDTH)), int(yPixel + (self.level[1] * LVLHEIGHT)))) == ITEMDICT['grey floor']:
                    objects.blockList.append(blocks.basicBlock('grey_block.png', (xPixel*BLOCKSIZE), (yPixel*BLOCKSIZE)))
                elif self.sprite.get_at((int(xPixel + (self.level[0] * LVLWIDTH)), int(yPixel + (self.level[1] * LVLHEIGHT)))) == ITEMDICT['metal floor']:
                    objects.blockList.append(blocks.basicBlock('metal_floor.png', (xPixel*BLOCKSIZE), (yPixel*BLOCKSIZE)))
                elif self.sprite.get_at((int(xPixel + (self.level[0] * LVLWIDTH)), int(yPixel + (self.level[1] * LVLHEIGHT)))) == ITEMDICT['metal solid']:
                    objects.blockList.append(blocks.basicBlock('metal_wall_solid.png', (xPixel*BLOCKSIZE), (yPixel*BLOCKSIZE)))
                elif self.sprite.get_at((int(xPixel + (self.level[0] * LVLWIDTH)), int(yPixel + (self.level[1] * LVLHEIGHT)))) == ITEMDICT['metal wallL']:
                    objects.blockList.append(blocks.basicBlock('metal_wallL.png', (xPixel*BLOCKSIZE), (yPixel*BLOCKSIZE)))
                elif self.sprite.get_at((int(xPixel + (self.level[0] * LVLWIDTH)), int(yPixel + (self.level[1] * LVLHEIGHT)))) == ITEMDICT['metal wallR']:
                    objects.blockList.append(blocks.basicBlock('metal_wallR.png', (xPixel*BLOCKSIZE), (yPixel*BLOCKSIZE)))
                elif self.sprite.get_at((int(xPixel + (self.level[0] * LVLWIDTH)), int(yPixel + (self.level[1] * LVLHEIGHT)))) == ITEMDICT['metal cornerBL']:
                    objects.blockList.append(blocks.basicBlock('metal_cornerBL.png', (xPixel*BLOCKSIZE), (yPixel*BLOCKSIZE)))
                elif self.sprite.get_at((int(xPixel + (self.level[0] * LVLWIDTH)), int(yPixel + (self.level[1] * LVLHEIGHT)))) == ITEMDICT['metal cornerBR']:
                    objects.blockList.append(blocks.basicBlock('metal_cornerBR.png', (xPixel*BLOCKSIZE), (yPixel*BLOCKSIZE)))
                elif self.sprite.get_at((int(xPixel + (self.level[0] * LVLWIDTH)), int(yPixel + (self.level[1] * LVLHEIGHT)))) == ITEMDICT['metal cornerTL']:
                    objects.blockList.append(blocks.basicBlock('metal_cornerTL.png', (xPixel*BLOCKSIZE), (yPixel*BLOCKSIZE)))
                elif self.sprite.get_at((int(xPixel + (self.level[0] * LVLWIDTH)), int(yPixel + (self.level[1] * LVLHEIGHT)))) == ITEMDICT['metal cornerTR']:
                    objects.blockList.append(blocks.basicBlock('metal_cornerTR.png', (xPixel*BLOCKSIZE), (yPixel*BLOCKSIZE)))
                elif self.sprite.get_at((int(xPixel + (self.level[0] * LVLWIDTH)), int(yPixel + (self.level[1] * LVLHEIGHT)))) == ITEMDICT['door']:
                    objects.blockList.append(blocks.basicBlock('lock_door.png', (xPixel*BLOCKSIZE), (yPixel*BLOCKSIZE)))
                elif self.sprite.get_at((int(xPixel + (self.level[0] * LVLWIDTH)), int(yPixel + (self.level[1] * LVLHEIGHT)))) == ITEMDICT['door top']:
                    objects.blockList.append(blocks.basicBlock('lock_door_top.png', (xPixel*BLOCKSIZE), (yPixel*BLOCKSIZE)))
                elif self.sprite.get_at((int(xPixel + (self.level[0] * LVLWIDTH)), int(yPixel + (self.level[1] * LVLHEIGHT)))) == ITEMDICT['light']:
                    objects.blockList.append(blocks.basicBlock('light.png', (xPixel*BLOCKSIZE), (yPixel*BLOCKSIZE)))
                elif self.sprite.get_at((int(xPixel + (self.level[0] * LVLWIDTH)), int(yPixel + (self.level[1] * LVLHEIGHT)))) == ITEMDICT['white cealing']:
                    objects.blockList.append(blocks.basicBlock('white_cealing.png', (xPixel*BLOCKSIZE), (yPixel*BLOCKSIZE)))
                elif self.sprite.get_at((int(xPixel + (self.level[0] * LVLWIDTH)), int(yPixel + (self.level[1] * LVLHEIGHT)))) == ITEMDICT['broken floor']:
                    objects.enemyList.append(blocks.brokenBlock('cracked_metal_floor.png',(xPixel*BLOCKSIZE), (yPixel*BLOCKSIZE)))
                elif self.sprite.get_at((int(xPixel + (self.level[0] * LVLWIDTH)), int(yPixel + (self.level[1] * LVLHEIGHT)))) == ITEMDICT['broken solid']:
                    objects.enemyList.append(blocks.brokenBlock('broken_solid.png',(xPixel*BLOCKSIZE), (yPixel*BLOCKSIZE)))

                elif self.sprite.get_at((int(xPixel + (self.level[0] * LVLWIDTH)), int(yPixel + (self.level[1] * LVLHEIGHT)))) == ITEMDICT['checkpoint']:
                    objects.checkpoint = checkpoint.checkpoint((xPixel*BLOCKSIZE), (yPixel*BLOCKSIZE))
                    
                elif self.sprite.get_at((int(xPixel + (self.level[0] * LVLWIDTH)), int(yPixel + (self.level[1] * LVLHEIGHT)))) == ITEMDICT['jet pack']:
                    objects.decalList.append(powerups.jetPack((xPixel*BLOCKSIZE)+2, (yPixel*BLOCKSIZE)))
                elif self.sprite.get_at((int(xPixel + (self.level[0] * LVLWIDTH)), int(yPixel + (self.level[1] * LVLHEIGHT)))) == ITEMDICT['teleport']:
                    objects.decalList.append(powerups.teleport((xPixel*BLOCKSIZE)+2, (yPixel*BLOCKSIZE)+2))
                
                elif self.sprite.get_at((int(xPixel + (self.level[0] * LVLWIDTH)), int(yPixel + (self.level[1] * LVLHEIGHT)))) == ITEMDICT['health']:
                    objects.health_battery.append(powerups.health((xPixel*BLOCKSIZE), (yPixel*BLOCKSIZE)))
                elif self.sprite.get_at((int(xPixel + (self.level[0] * LVLWIDTH)), int(yPixel + (self.level[1] * LVLHEIGHT)))) == ITEMDICT['battery']:
                    objects.health_battery.append(powerups.battery((xPixel*BLOCKSIZE), (yPixel*BLOCKSIZE)))
                        
                elif self.sprite.get_at((int(xPixel + (self.level[0] * LVLWIDTH)), int(yPixel + (self.level[1] * LVLHEIGHT)))) == ITEMDICT['ball enemy']:
                    objects.enemyList.append(enemies.ball((xPixel*BLOCKSIZE), (yPixel*BLOCKSIZE)))
                elif self.sprite.get_at((int(xPixel + (self.level[0] * LVLWIDTH)), int(yPixel + (self.level[1] * LVLHEIGHT)))) == ITEMDICT['robot enemy']:
                    objects.enemyList.append(enemies.robot((xPixel*BLOCKSIZE), (yPixel*BLOCKSIZE)))
                elif self.sprite.get_at((int(xPixel + (self.level[0] * LVLWIDTH)), int(yPixel + (self.level[1] * LVLHEIGHT)))) == ITEMDICT['floor spike']:
                    objects.enemyList.append(enemies.spike((xPixel*BLOCKSIZE), (yPixel*BLOCKSIZE)))
                else: pass



class background():
    def __init__(self):
        self.sprite = data.load_image('lightBlueBgd.png', 0)

    def draw(self):
        game_vars.screen.blit(self.sprite, (0,  0))
