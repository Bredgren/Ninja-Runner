import pygame, os
import game_vars, level, objects, player, misc, checkpoint, data, button, random
from constants import *

def initGame(width, height, caption):
    #setup pygame
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    loadSfx()

    #setup screen
    game_vars.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption(caption)
    icon = data.load_image('icon_img.png')
    pygame.display.set_icon(icon)

    #setup clock
    game_vars.clock = pygame.time.Clock()

    #Start Music
    playMusic()
    
def startGame():
    #Setup Objects
    try:
        level.levelSpawner = level.levelSpawner()
        level.background = level.background()
    except: pass
    objects.player = player.player(PLAYERSTART[0],PLAYERSTART[1])
    objects.energyBar = misc.energyBar()
    objects.healthBar = misc.healthBar()


def printText(inputText, inputSize, inputX, inputY, inputColor, tl=0):
    font = pygame.font.SysFont("arial", inputSize)
    text = font.render((str(inputText)), 1, inputColor)
    if inputX == -1:
        xPos = game_vars.width/2
    else:
        xPos = inputX
    if inputY == -1:
        yPos = game_vars.height/2
    else:
        yPos = inputY
    if tl:
        textPosition = text.get_rect(left = xPos, top = yPos)
    else:
        textPosition = text.get_rect(centerx = xPos, centery = yPos)
    game_vars.screen.blit(text, textPosition)


def playMusic():
    music = random.choice(MUSIC)
    fileLocation = os.path.join('data', music)
    pygame.mixer.music.load(fileLocation)
    pygame.mixer.music.set_endevent(32)
    pygame.mixer.music.play()

def updateMusic():
    #for event in game_vars.events:
    #    if event.type == 32:
    if not pygame.mixer.music.get_busy():
            playMusic()

def loadSfx():
    game_vars.ball_death = data.load_sound('ball_death.wav')
    game_vars.ball_hit_wall = data.load_sound('ball_hit_wall.wav')
    game_vars.ball_hit_wall.set_volume(.2)
    game_vars.battery_pickup = data.load_sound('battery.wav')
    game_vars.check = data.load_sound('checkpoint.wav')
    game_vars.heal = data.load_sound('heal.wav')
    game_vars.robot_death = data.load_sound('robot_death.wav')
    game_vars.robot_hit_wall = data.load_sound('robot_hit_wall.wav')
    game_vars.robot_hit_wall.set_volume(.2)
    game_vars.teleport = data.load_sound('teleport.wav')
    game_vars.throw = data.load_sound('throw.wav')
    game_vars.block_hit = data.load_sound('block_hit.wav')
    game_vars.jet_pack = data.load_sound('jetpack.wav')


def keyPressed(inputKey):
    keysPressed = pygame.key.get_pressed()
    if keysPressed[inputKey]:
        return True
    else:
        return False


def checkCollision(inputObject1, inputObject2):
    if inputObject1.xPos + inputObject1.width  >= inputObject2.xPos and inputObject1.xPos <= inputObject2.xPos + inputObject2.width:
        if inputObject1.yPos + inputObject1.height  >= inputObject2.yPos and inputObject1.yPos <= inputObject2.yPos + inputObject2.height:
            return True
        else:
            return False
    else:
        return False

def refreshLevelData():
    objects.lvl_names, objects.times, objects.player_pos, objects.beatTimes = data.readFile('level data.txt')

    objects.levelButtonList = []
    objects.timeList = []
    for lvl in range(len(objects.lvl_names)):
        objects.levelButtonList.append(button.textButton('%s' %objects.lvl_names[lvl], 40, 0, -50))
        objects.timeList.append(button.textButton('%s s' %float(objects.times[lvl]), 30, 0, -50))
        objects.beatList.append(button.textButton('%s s' %float(objects.beatTimes[lvl]), 30, 0, -50))


def gameReset():
    refreshLevelData()
    game_vars.gameScreen = "intro"
    game_vars.introScreen = 'main'
    game_vars.firstCall = True
    game_vars.powerJetPack = False
    game_vars.powerTeleport = False
    game_vars.levelName = ''
    game_vars.saveLevel = [1, 1]
    game_vars.saveXPos = PLAYERSTART[0]
    game_vars.saveYPos = PLAYERSTART[1]
    game_vars.time = 0
    del objects.enemyList[:]
    del objects.blockList[:]
    del objects.decalList[:]
    del objects.bulletList[:]
    del objects.health_battery[:]
    try:
        del objects.checkpoint
    except:
        pass
    try:
        level.levelSpawner.reset()
    except: pass

def changeLevel(newLevelX, newLevelY):
    level.levelSpawner.level = [newLevelX, newLevelY]
    del objects.enemyList[:]
    del objects.blockList[:]
    del objects.decalList[:]
    del objects.bulletList[:]
    del objects.health_battery[:]
    try:
        del objects.checkpoint
    except:
        pass
    level.levelSpawner.draw()

