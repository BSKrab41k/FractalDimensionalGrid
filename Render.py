import pygame 
from Colors import *


cellsize = 10
res = width, height = (1366, 768)
gridres = gridwidth, gridheight = (width//cellsize, height//cellsize)
pygame.init()
screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()
FPS = 60
screen.fill(Colors['BGCOLOR'])

def UpdateScreen():
    pygame.display.update()
    clock.tick(FPS)
    pygame.display.set_caption(f'-=<Cell Of Imaginarium>=-   FPS = {round(clock.get_fps(), 1)}')
    
def CellRender(x, y, cellsize):
    pass