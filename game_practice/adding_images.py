'''
Created on 19-Jun-2020

@author: Toshinee Bhasin
'''
import pygame
from builtins import *

#initialize the pygame
pygame.init()

#create the screen
screen =  pygame.display.set_mode((800, 600))

#uploading player image
playerImg = pygame.image.load("spaceship.png")
playerx = 370
playery = 480

#function to display player
def player():
    screen.blit(playerImg,(playerx,playery))
    

#title and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

 


#game loop
running = True
while running:
    #RGB = Red, Green, Blue
    screen.fill((0,0,0))   #black color
    #playery -= 0.1       to move upward direction
    #playerx += 0.1       to move at right
    #playerx -= 0.1       to move left
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
     
    player()       
    pygame.display.update()    #(255,0,0)   red
