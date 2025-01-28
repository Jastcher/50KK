import pygame
import time
import numpy as np

from ray import *
from scene import *
from sphere import *

pygame.init()

aspectRatio = 16.0 / 9.0
imageWidth = 500
imageHeight = int(imageWidth / aspectRatio)

screen = pygame.display.set_mode([imageWidth, imageHeight])

# world
world = Scene([Sphere([0,0,-0.5], 0.2)])

viewportHeight = 2.0
viewportWidth = aspectRatio * viewportHeight
focalLength = 1.0

origin = np.array([0, 0, 0])
horizontal = np.array([viewportWidth, 0, 0])
vertical = np.array([0, viewportHeight, 0])
lowerLeftCorner = origin - horizontal/2 - vertical/2 - np.array([0, 0, focalLength])

def UnitVector(vec):
    return vec / (vec**2).sum()**0.5

def FragmentShader(u, v):
    r = Ray(origin, lowerLeftCorner + u*horizontal + v*vertical - origin)

    record = [HitRecord()]
    if (world.Trace(r, 0.01, float('inf'), record)):
        return 0.5 * (record[0].normal + np.array([1,1,1])) * 255
    
    unitDirection = -UnitVector(r.direction)
    t = 0.5*(unitDirection[1] + 1.0)

    color = (1.0-t)*np.array([1.0, 1.0, 1.0]) + t*np.array([0.5, 0.7, 1.0])
    color *= 255
    #print(color)
    return color
    

def Main():
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return

    for i in range(imageHeight):
        for j in range(imageWidth):
            
            u = float(j) / (imageWidth-1)
            v = float(i) / (imageHeight-1)

            screen.set_at((j, i), FragmentShader(u, v))
            
        pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

Main()
pygame.quit()