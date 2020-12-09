import pygame, random, sys
from pygame.locals import *
from pygame.key import *

def set_Background():
    screen = pygame.display.set_mode((500,500))
    surface = pygame.image.load('Background.png')
    surface = pygame.transform.scale(surface, (500, 500))
    screen.blit(surface, (0,0))
    pygame.display.update()
    return screen

def set_Enemy():
    enemy = pygame.image.load('Enemy.png')
    enemy = pygame.transform.scale(enemy, (50, 50))
    return enemy

def set_Player():
    player = pygame.image.load('Player.png')
    player = pygame.transform.scale(player, (70, 70))
    return player

RUNNING = True

while RUNNING:
    background = set_Background()
    enemy = set_Enemy()
    player = set_Player()
    enemy_rect = enemy.get_rect()
    player_rect = player.get_rect()

    e_x = random.randint(10,450)
    e_y = random.randint(10,450)
    background.blit(enemy, (e_x, e_y))
    pygame.display.update()

    for event in pygame.event.get():
        key = pygame.key.get_pressed()
        if event.type == key[pygame.K_ESCAPE]: 
        #module pygame has no K_ESCAPE member
            sys.exit()
        if event.type == pygame.QUIT: 
        #says module pygame has no QUIT member
            sys.exit()