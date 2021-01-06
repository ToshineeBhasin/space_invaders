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

#title and icon
pygame.display.set_caption("Spave Invader")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
            
#RGB = Red, Green, Blue
screen.fill((255,0,0))   #black color
pygame.display.update()    #(255,0,0)   red
