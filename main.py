import os
# Import the libraries
import pygame
from static import *
from Button import *

# Initialise the engines
pygame.init()



def Home():  # This is the home page of my pong game
    click = False
    while True:

        mx, my = pygame.mouse.get_pos()
        mouse = (mx, my)
        gameDisplay.fill(black)
        PongButton = pygame.Rect(20, 150, 250, 60)
        SpaceButton = pygame.Rect(20, 250, 250, 60)

        PongButtonText = Button("Pong", 20, 150, font)
        SpaceButtonText = Button("Space Invaders", 20, 250, font)

        PongButtonText.write(gameDisplay, red)
        SpaceButtonText.write(gameDisplay, red)

        if PongButton.collidepoint(mouse):
            PongButtonText.write(gameDisplay, lightred)
            if click:
                Pong()

        if SpaceButton.collidepoint(mouse):
            SpaceButtonText.write(gameDisplay, lightred)
            if click:
                Space()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()


def Pong():
    click = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        gameDisplay.fill(black)
        pygame.draw.rect(gameDisplay, blue, [100, 100, 100, 100])
        pygame.display.update()


gameDisplay = pygame.display.set_mode(ScreenSize)
pygame.display.set_caption("Pong")


def Space():
    click = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        gameDisplay.fill(black)
        pygame.display.update()


Home()
