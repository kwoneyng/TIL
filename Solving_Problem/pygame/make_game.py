import pygame
import time
import math
import random
from random import *
from pygame.locals import*
from datetime import datetime
from datetime import timedelta
FPS = 30
fpsClock = pygame.time.Clock()

def draw_block(screen, color, position):
    block = pygame.Rect((position[1], position[0]), (20,20))
    pygame.draw.rect(screen, color, block)


def draw_background(screen):
    background = pygame.Rect((0,0), (width, height))
    pygame.draw.rect(screen, blue, background)

pygame.init()
width, height = 1040, 680
screen = pygame.display.set_mode((width,height))

red = 255,0,0
green = 0,255,0
blue = 0,0,255
black = 0,0,0
white = 255,255,255

# class ----------------------------------------------------

class Player:
    color = green

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

class Enermies:
    color = red
    def __init__(self):
        self.speed = 5
        self.stats = []  # stats = [hp, position]

    def draw(self, screen):
        for hp, y, x in self.stats:
            draw_block(screen, self.color, (y,x))

class GameBoard:
    width = 1040
    height = 680

    def __init__(self):
        self.player = Player()
        self.castle = Castle()
        self.block = Block()
        self.arrows = Arrows()
        self.enermies = Enermies()

    def draw(self, screen):
        self.player.draw(screen)
        self.castle.draw(screen)
        self.block.draw(screen)
        self.arrows.draw(screen)
        self.enermies.draw(screen)

class Arrows:
    color = white
    def __init__(self):
        self.stats = []

    def draw(self, screen):
        for pal, y, x in self.stats:
            draw_block(screen, self.color, (y,x))

#--------------------------------------------------------------

game_board = GameBoard()

moveLeft=False
moveRight = False
moveUp = False
moveDown = False
MOVESPEED = 0.05
acc = [0,0]
arrows = []
cur_enermy = 0
score = 0
arrow_flag = 0
while True:
    if random() < 0.1:
        if cur_enermy < 5:
            game_board.enermies.stats.append([10,game_board.width-5,random()*game_board.height])
            print('나타나')
            cur_enermy += 1
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            print(score)
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
            position = (event.pos[1], event.pos[0])
            if arrow_flag == 1:
                if datetime.now() - shoot_time > timedelta(seconds=0.1):
                    game_board.arrows.stats.append([math.atan2(position[0]-game_board.player.position[0], position[1]-game_board.player.position[1]),game_board.player.position[1], game_board.player.position[0]])
                    shoot_time = datetime.now()
                    acc[1] += 1
            # print('움직이는중')
            # game_board.block.positions.append(position)
        if event.type == pygame.MOUSEBUTTONDOWN:
            # position = pygame.mouse.get_pos()
            position = (event.pos[1], event.pos[0])
            arrow_flag = 1
            shoot_time = datetime.now()
        if event.type == pygame.MOUSEBUTTONUP:
            arrow_flag = 0
    die = []
    for bullet in game_board.arrows.stats:
        index = 0
        velx=math.cos(bullet[0])*1
        vely=math.sin(bullet[0])*1
        bullet[1] += velx
        bullet[2] += vely
        for enermy in game_board.enermies.stats:
            if abs(enermy[1] - bullet[1]) <= 0.1 and abs(enermy[2] - bullet[2]) <= 0.1:
                die.append(enermy)
        if bullet[1] < 6 or bullet[1] > game_board.width or bullet[2] < 0 or bullet[2] > game_board.height:
            game_board.arrows.stats.pop(index)
        index += 1
    if die:
        print(die)
    for enermy in game_board.enermies.stats:
        index1 = 0
        for d in die:
            if d == enermy:
                game_board.enermies.stats.pop(index1)
                cur_enermy -= 1
                score += 1
                print(d, enermy)
                continue

        if enermy[1] > 6:
            enermy[1] -= 1

        if enermy[0] == 0 or enermy[1] > game_board.width or enermy[2] < 0 or enermy[2] > game_board.height:
            game_board.enermies.stats.pop(index1)
            cur_enermy -= 1
        index1 += 1


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