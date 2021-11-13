import pygame, os, os.path

# Data Functions
def load_image(name, colorkey=None):
    """Loads an image, prepares it for play.
       If colorkey is -1 the top left corner or the image will be used."""
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(fullname, pygame.get_error()))

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
            image = image.convert()
        else:
            image = image.convert_alpha()
        image.set_colorkey(colorkey, pygame.RLEACCEL)

    return image

def load_sound(name):
    """Loads a sound, prepares it for play."""
    class NoneSound:
        def play(self):
            pass

    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()

    fullname = os.path.join('data', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error:
        print('Warning, unable to load, %s' % fullname)

    return sound

def readFile(name):
    lvl_names =[]
    times = []
    player_pos = []
    beatTimes = []
    fullname = os.path.join('data', name)
    with open(fullname, 'r') as f:
        for line in f:
            line = line.rstrip()
            info = line.split(':')
            lvl_names.append(info[0])
            times.append(info[1])
            player_pos.append([int(info[2]), int(info[3])])
            beatTimes.append(info[4])

    return lvl_names, times, player_pos, beatTimes

def writeFile(name, lvl_names, times, player_pos, beatTimes):
    fullname = os.path.join('data', name)
    with open(fullname, 'w') as f:
        for line in range(len(lvl_names)):
            print(":".join(str(i) for i in (lvl_names[line], times[line], player_pos[line][0], player_pos[line][1], beatTimes[line])),
                  file=f)
