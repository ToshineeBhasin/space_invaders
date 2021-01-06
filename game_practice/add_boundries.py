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
playerx_change = 0
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
        #adding keyboard input control
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:            #means if any key is pressed
            if event.key == pygame.K_RIGHT:
                playerx_change = 0.3
            if event.key == pygame.K_LEFT:
                playerx_change = -0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerx_change = 0
        
        
        
        
        
    playerx += playerx_change    
    
    if playerx <=0:
        playerx = 0
    elif playerx >=730:
        playerx = 730
    player()       
    pygame.display.update()    #(255,0,0)   red
