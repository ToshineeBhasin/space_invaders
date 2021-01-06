'''
Created on 19-Jun-2020

@author: Toshinee Bhasin
'''
import pygame
pygame.init()    #initialise pygame

#creating screen
screen = pygame.display.set_mode((800,600))
running  = True
#game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    