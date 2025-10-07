import pygame
explosion_1 = None
explosion_2 = None
def init():    
    global explosion_1, explosion_2
    pygame.mixer.init()
    explosion_1 = pygame.mixer.Sound('Five/explosion.wav')
    explosion_1.set_volume(0.1)
    explosion_2 = pygame.mixer.Sound('Five/explosion2.wav')
    explosion_2.set_volume(0.2)

def playmusic():
    pygame.mixer.music.load('./Five/battle.mp3')
    pygame.mixer.music.set_volume(0.04)
    pygame.mixer.music.play(-1)

def play_explosion_1():
    explosion_1.play()

def play_explosion_2():
    explosion_2.play()

if __name__ == '__main__':
    import time
    init()
    play_explosion_1()
    time.sleep(2)
    play_explosion_2()
    time.sleep(2)
    playmusic()
    time.sleep(5)
