# Import libraries
import os
import pygame

pygame.init()

ScreenSizeInfo = pygame.display.Info()  # Get the info for the size of the monitor
ScreenSize = (ScreenSizeInfo.current_w, ScreenSizeInfo.current_h)  # Define the size of the screen

# Colours
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0,255,0)
lightred = (100,0,0)
font = pygame.font.SysFont('courier', 35, True, False)
