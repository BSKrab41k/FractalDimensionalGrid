from FractalDimensionalGrid import *
from Render import *
import pygame



run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    CellSearcher(grid, 0)
    UpdateScreen()
pygame.quit()
    