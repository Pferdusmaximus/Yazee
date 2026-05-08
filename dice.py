import pygame, random
PIP_POS = {
    1: [(0.5,0.5)],
    2: [(0.25,0.25),(0.75,0.75)],
    3: [(0.25,0.25),(0.5,0.5),(0.75,0.75)],
    4: [(0.25,0.25),(0.75,0.25),(0.25,0.75),(0.75,0.75)],
    5: [(0.25,0.25),(0.75,0.25),(0.5,0.5),(0.25,0.75),(0.75,0.75)],
    6: [(0.25,0.2),(0.25,0.5),(0.25,0.8),(0.75,0.2),(0.75,0.5),(0.75,0.8)]
}

class Dice:
    def __init__(self, value, size, position, colour):
        self.value = value
        self.size = size
        self.position = position
        self.colour = colour


    def draw(self, window):
        x,y = self.position; w,h = self.size
        pygame.draw.rect(window, self.colour, (x,y,w,h))
        pygame.draw.rect(window, (0,0,0), (x,y,w,h), 2)
        r = max(2, min(w,h)//12)
        for fx,fy in PIP_POS[int(self.value)]:
            pygame.draw.circle(window, (0,0,0), (int(x+fx*w), int(y+fy*h)), r)

