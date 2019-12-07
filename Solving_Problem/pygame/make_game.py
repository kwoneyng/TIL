import pygame
import time
import math
import random
from pygame.locals import*
from datetime import datetime
from datetime import timedelta
FPS = 30
fpsClock = pygame.time.Clock()

def draw_block(screen, color, position):
    block = pygame.Rect((position[1]*BLOCK_SIZE, position[0]*BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, color, block)


def draw_background(screen):
    background = pygame.Rect((0,0), (width, height))
    pygame.draw.rect(screen, blue, background)

pygame.init()
width, height = 1040, 680
BLOCK_SIZE = 20
screen = pygame.display.set_mode((width,height))

red = 255,0,0
green = 0,255,0
blue = 0,0,255
black = 0,0,0
white = 255,255,255

# class ----------------------------------------------------

class Player:
    color = red

    def __init__(self):
        self.position = [30, 30]
    
    def draw(self, screen):
        draw_block(screen, self.color, self.position)


class Castle:
    color = black
    def __init__(self):
        self.positions = []
        for x in range(52):
            for y in range(6):
                self.positions.append([x,y])
    
    def draw(self, screen):
        for position in self.positions:
            draw_block(screen, self.color, position)


class Block:
    color = white
    def __init__(self):
        self.positions = []
    
    def draw(self, screen):
        for position in self.positions:
            draw_block(screen, self.color, position)


class GameBoard:
    width = 52
    height = 34

    def __init__(self):
        self.player = Player()
        self.castle = Castle()
        self.block = Block()
        self.arrows = Arrows()

    def draw(self, screen):
        self.player.draw(screen)
        self.castle.draw(screen)
        self.block.draw(screen)
        self.arrows.draw(screen)

class Arrows:
    color = white
    def __init__(self):
        self.stats = []

    def draw(self, screen):
        for pal, x, y in self.stats:
            draw_block(screen, self.color, (y,x))

#--------------------------------------------------------------

game_board = GameBoard()

moveLeft=False
moveRight = False
moveUp = False
moveDown = False
MOVESPEED = 0.1
acc = [0,0]
arrows = []

while True:
    time.sleep(0.005)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT or event.key == ord('a'):
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == ord('d'):
                moveRight = True
                moveLeft = False
            if event.key == K_UP or event.key == ord('w'):
                moveUp = True
                moveDown = False
            if event.key == K_DOWN or event.key == ord('s'):
                moveUp = False
                moveDown = True
        if event.type == pygame.KEYUP:
            if event.key == K_LEFT or event.key == ord('a'):
                moveLeft = False
            if event.key == K_RIGHT or event.key == ord('d'):
                moveRight = False
            if event.key == K_UP or event.key == ord('w'):
                moveUp = False
            if event.key == K_DOWN or event.key == ord('s'):
                moveDown = False
        if event.type == pygame.MOUSEMOTION:
            position = (event.pos[1]//BLOCK_SIZE, event.pos[0]//BLOCK_SIZE)
            # print('움직이는중')
            # game_board.block.positions.append(position)
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            acc[1] += 1
            game_board.arrows.stats.append([math.atan2(position[0]-game_board.player.position[0], position[1]-game_board.player.position[1]),game_board.player.position[1], game_board.player.position[0]])
            print('눌렀다', position)
            print(arrows)

    for bullet in game_board.arrows.stats:
        index = 0
        velx=math.cos(bullet[0])*1
        vely=math.sin(bullet[0])*1
        bullet[1] += velx
        bullet[2] += vely
        if bullet[1] < 6 or bullet[1] > game_board.width or bullet[0] < 0 or bullet[0] > game_board.height:
            game_board.arrows.stats.pop(index)
        index += 1

    if moveDown and game_board.player.position[0]+1 < game_board.height:
        game_board.player.position[0] += MOVESPEED
    if moveUp and game_board.player.position[0] > 0:
        game_board.player.position[0] -= MOVESPEED
    if moveLeft and game_board.player.position[1] > 6:
        game_board.player.position[1] -= MOVESPEED
    if moveRight and game_board.player.position[1]+1 < game_board.width:
        game_board.player.position[1] += MOVESPEED

    draw_background(screen)
    # print(game_board.player.position)
    game_board.draw(screen)
    pygame.display.update()    