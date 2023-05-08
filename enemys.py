from random import *

import pygame

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400


class Asteroid:
    def __init__(self):
        self.asteroid_x = randrange(SCREEN_HEIGHT)
        self.asteroid_y = 0

        self.asteroid = pygame.image.load('Astreroïd_2.png')
        self.pos_asteroid = self.asteroid.get_rect(x=self.asteroid_x, y=self.asteroid_y)

        self.speed = 2.5
        self.velocity = [0,1]

    def move(self):
        self.pos_asteroid.move_ip(self.speed * self.velocity[0], self.speed * self.velocity[1])

        if self.pos_asteroid.y >= SCREEN_WIDTH:
            self.asteroid_x = randrange(SCREEN_HEIGHT)
            self.asteroid_y = 0
            self.pos_asteroid = self.asteroid.get_rect(x=self.asteroid_x, y=self.asteroid_y)
            self.speed += 1


    def draw(self, surface):
        surface.blit(self.asteroid, self.pos_asteroid)
