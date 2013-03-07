import game_vars, pygame

# WIDOW SIZE #
WIN_HEIGHT    = 600
WIN_WIDTH     = 600

# MUSIC #
MUSIC = ['Ghostpocalypse - 7 Master.ogg',
         'Intended Force.ogg',
         'Kick Shock.ogg',
         'Mistake the Getaway.ogg',
         'MTA.ogg',
         'Padanaya Blokov.ogg',
         'Rocket.ogg']

# LEVEL STUFF #
GAMEWIDTH     = 2
GAMEHEIGHT    = 1
LVLWIDTH      = 30
LVLHEIGHT     = 30
BLOCKSIZE     = 20 # size of each square block
ITEMDICT      = {
                 'grey floor':    (255,0,0),
                 'metal floor':   (0,0,0),
                 'metal solid':   (100,100,100),
                 'metal wallL':   (120,0,0),
                 'metal wallR':   (0,120,0),
                 'metal cornerBL':(0,0,120),
                 'metal cornerBR':(0,0,255),
                 'metal cornerTL':(120,120,0),
                 'metal cornerTR':(120,200,0),
                 'door':          (120,120,255),
                 'door top':      (120,255,120),
                 'light':         (255,255,120),
                 'white cealing': (200,200,200),
                 'jet pack':      (255,120,0),
                 'teleport':      (120,255,255),
                 'health':        (0,255,0),
                 'battery':       (255,255,0),
                 'ball enemy':    (120,0,120),
                 'robot enemy':   (120,0,255),
                 'broken floor':  (255,0,120),
                 'broken solid':  (255,120,120),
                 'floor spike':   (255,0,255),
                 'checkpoint':    (255,120,255)
                }

# PLAYER #
PLAYERSTART   = (LVLWIDTH * 5, WIN_HEIGHT - (LVLWIDTH * 2))
PLAYERSPEED   = 7
BULLETSPEED   = 15
RELOAD_TIME   = 5
JUMP_FORCE    = 15.0
FLY_FORCE     = 3
GRAVITY       = 2

# BALL ENEMY #
BALLSPEED     = 3
BALL_LIVES    = 2
BALLDAMAGE    = 5

# ROBOT ENEMY #
ROBOTSPEED    = 4
ROBOT_LIVES   = 1
ROBOTDAMAGE   = 10

# FALLING BLOCK #
FALLSPEED     = 13
FALLDELAY     = 5
FALLDAMAGE    = 20

# FLOOR SPIKE #
SPIKEDAMAGE   = 20

# COLORS #
BLACK         = pygame.Color('black')
LIGHTGREY     = pygame.Color('light grey')
WHITE         = pygame.Color('white')
LIGHTBLUE     = pygame.Color('light blue')
DARKBLUE      = pygame.Color('dark blue')
GREEN         = pygame.Color('green')
