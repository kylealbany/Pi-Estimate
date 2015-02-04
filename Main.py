__author__ = 'Kyle'
from time import sleep
from math import hypot
from random import uniform
import pygame

pygame.init()

maxTrials=100000000 # total number of trials to do before stopping
trials=0 # total number of (x,y) pairs generated
successes=0 # number of times the (x,y) pair is within the circle
windowSize=500 # length and width in pixels of the window
lineWidth=3 # thickness of the drawn circle and square
squareWidth=400 # width of square, determines most other variables. Can't be greater than windowSize
sleepInterval=0 # seconds to wait in between each point
font=pygame.font.SysFont("arial", (windowSize-squareWidth)/6) # font and size to use for text

# create window and draw circle/rectangle borders
window= pygame.display.set_mode((windowSize,windowSize))
pygame.draw.circle(window, (255,255,255), (windowSize/2,windowSize/2), squareWidth/2, lineWidth)
pygame.draw.rect(window, (255,255,255),((windowSize-squareWidth)/2,(windowSize-squareWidth)/2,squareWidth,squareWidth),lineWidth)
pygame.display.update()

while trials<maxTrials:
    trials+=1
    x=uniform((windowSize-squareWidth)/2,(windowSize-squareWidth)/2+squareWidth)
    y=uniform((windowSize-squareWidth)/2,(windowSize-squareWidth)/2+squareWidth)
    sleep(sleepInterval)
    # is inside circle
    if hypot(x-windowSize/2,y-windowSize/2)<=squareWidth/2:
        successes+=1
        pygame.draw.circle(window, (0,255,0), (int(x),int(y)),1, 0)
        pygame.display.update()
    # isn't inside circle
    else:
        pygame.draw.circle(window, (255,0,0), (int(x),int(y)),1, 0)
        pygame.display.update()
    string1= "Current estimate of pi: " + "%.10f"%(4*float(successes)/trials) + "       "
    string2= str(trials) + " points generated        "
    title1=font.render(string1, 1, (255,255,255),(0,0,0))
    title2=font.render(string2, 1, (255,255,255),(0,0,0))
    window.blit(title1,(0,0))
    window.blit(title2,(0,(windowSize-squareWidth)/6+4))