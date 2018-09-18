#!usr/bin/env /python
#
# Filename : sprites.py
# Author : Juhana Kammonen 25.08.2009 - for JukiWeb Merseine
# Purpose : the file for all sprite classes needed by game MitoBlaster

import pygame

class PointerL(pygame.sprite.Sprite):
    def __init__(self, initial_position):

        self.image = pygame.image.load('data/pointer_1l.PNG')
        self.original = True

        # Make our top-left corner the passed-in location:
        self.rect = self.image.get_rect()
        self.rect.topleft = initial_position
	self.next_update_time = 0 # update() not called yet

    def update(self, current_time, initial_position):

        self.rect = self.image.get_rect()
        self.rect.topleft = initial_position
        
        # in case it's time to update:
        if self.next_update_time < current_time:
            
            if self.original == True: # if this is the original image
                self.image = pygame.image.load('data/pointer_1l_light.PNG')
                self.next_update_time = current_time + 75
                self.original = False
                self.original = False

            else:
                self.image = pygame.image.load('data/pointer_1l.PNG')
                self.next_update_time = current_time + 75
                self.original = True

class PointerR(pygame.sprite.Sprite):
    def __init__(self, initial_position):

        self.image = pygame.image.load('data/pointer_1r.PNG')
        self.original = True

        # Make our top-right corner the passed-in location:
        self.rect = self.image.get_rect()
        self.rect.topright = initial_position
	self.next_update_time = 0 # update() not called yet
	
	
    def update(self, current_time, initial_position):

        self.rect = self.image.get_rect()
        self.rect.topright = initial_position

        # in case it's time to update:
        if self.next_update_time < current_time:
                
            if self.original == True: # if this is the original image
                self.image = pygame.image.load('data/pointer_1r_light.PNG')
                self.next_update_time = current_time + 75
                self.original = False

            else:
                self.image = pygame.image.load('data/pointer_1r.PNG')
                self.next_update_time = current_time + 75
                self.original = True
