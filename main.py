#!usr/bin/env/ python
#
# Filename : main.py
# Author : Juhana Kammonen for Konekettu Sep 25 2018
# Purpose : MitoBlaster v0.1 main program file

import sys, pygame # brings on your system and your pygame module
import os.path # imports your operational system path

from pygame.locals import *
from sprites import * # import all sprites to the main file

selections = ["START", "OPTIONS", "STORY", "EXIT GAME"]
slct = 0 #idx of selection state
selection = selections[slct]
slct_changed = False
global event

def gimmeMain():

        global initialPositions, selections, slct, slct_changed

        nonePressed = True

        if pygame.mixer:
                pygame.mixer.set_num_channels(1)
                music = pygame.mixer.Sound('data/main.ogg')
                music.play(-1)
        
        newFont = pygame.font.Font('data/font/DOWN.TTF', 12)
        startText = newFont.render("START GAME", 1, (152, 251, 152))
        optionsText = newFont.render("OPTIONS", 1, (152, 251, 152))
        storyText = newFont.render("STORY", 1, (152, 251, 152))
        exitText = newFont.render("EXIT GAME", 1, (152, 251, 152))
        startTextPos = startText.get_rect(centerx=background.get_width()/2, centery=background.get_width()/2)
        optionsTextPos = optionsText.get_rect(centerx=background.get_width()/2, centery=background.get_width()/2 + 25)
        storyTextPos = storyText.get_rect(centerx=background.get_width()/2, centery=(background.get_width()/2 + 50))
        exitTextPos = storyText.get_rect(centerx=(background.get_width()/2)-16, centery=(background.get_width()/2 + 75))
        background.blit(startText, startTextPos)
        background.blit(optionsText, optionsTextPos)
        background.blit(storyText, storyTextPos)
        background.blit(exitText, exitTextPos)

        pointerL = PointerL(initialPositions[0]) # left pointer with start position at "START GAME"
        pointerR = PointerR(initialPositions[1]) # right pointer with start position at "START GAME"
        screen.blit(background, (22, 0))
        screen.blit(pointerL.image, pointerL.rect)
        screen.blit(pointerR.image, pointerR.rect)
        pygame.display.flip()

        pointerList = [pointerL, pointerR]

        while selection != "EXIT GAME":
                event = pygame.event.poll()
                if event.type != KEYDOWN:
                        rollMenuAnimation(pointerList)
                else:
                        handle(event, pointerList)
                        
                        # music change test (WORKS!)
                        if slct_changed == True:
                                if selection == "OPTIONS": 
                                        if pygame.mixer:
                                                music.stop()
                                                music = pygame.mixer.Sound('data/level_one.ogg')
                                                music.play(-1)
                                                slct_changed = False

        return("EXIT GAME")                

def handle(event, pointerList): # event handler

        global initialPositions, selection, slct, slct_changed
        print initialPositions
        print event

        if event.dict['key'] == 273:

                #Selection pointer up move:

                if (slct-1 < 0): # set pointers downmost
                        slct = 3
                        initialPositions = [[initialPositions[0][0], initialPositions[0][1]+(3*26)],
                                            [initialPositions[1][0], initialPositions[1][1]+(3*26)]]
                        screen.blit(background, (22, 0))
                        rollMenuAnimation(pointerList)

                else:
                        slct -= 1
                        initialPositions = [[initialPositions[0][0], initialPositions[0][1]-26],
                                            [initialPositions[1][0], initialPositions[1][1]-26]]
                        screen.blit(background, (22, 0))
                        rollMenuAnimation(pointerList) 
                
        elif event.dict['key'] == 274:
                
		#Selection pointer down move

                if (slct+1 >= len(selections)): # return pointers upmost
                        slct = 0
                        initialPositions = [[initialPositions[0][0], initialPositions[0][1]-(3*26)],
                                            [initialPositions[1][0], initialPositions[1][1]-(3*26)]]
                        screen.blit(background, (22, 0))
                        rollMenuAnimation(pointerList)                        
                else:
                        slct += 1
                        initialPositions = [[initialPositions[0][0], initialPositions[0][1]+26],
                                            [initialPositions[1][0], initialPositions[1][1]+26]]
                        screen.blit(background, (22, 0))
                        rollMenuAnimation(pointerList)


        elif event.dict['key'] == 13: # return key pressed
                selection = selections[slct]
                slct_changed = True
                
        else:
                print 'The key was irrelevant.'
		#TODO: Other functionality

def rollMenuAnimation(pointerList):

        global initialPositions
        
        time = pygame.time.get_ticks()
        for i, pointer in enumerate(pointerList):
            
            pointer.update(time, initialPositions[i])
            screen.blit(pointer.image, pointer.rect)
                                
        pygame.display.flip()
        return True

pygame.init() # initialize the pygame module

size = width, height = 600, 600

screen = pygame.display.set_mode(size)
pygame.display.set_caption('MitoBlaster v0.1')

background = pygame.image.load('data/main_screen.png')
background = background.convert()

if pygame.font:
    font = pygame.font.Font('data/font/DOWN.TTF', 24)
    text = font.render("MitoBlaster", 1, (152, 251, 152))
    textpos = text.get_rect(centerx=background.get_width()/2, centery=background.get_width()/3)
    background.blit(text, textpos)

screen.blit(background, (22, 0))
pygame.display.flip()

initialPositions = [[background.get_width()/2 - 75, background.get_width()/2 - 19],
                    [background.get_width()/2 + 120, background.get_width()/2 - 19]]

while selection != "EXIT GAME":
        selection = gimmeMain()

sys.exit()
