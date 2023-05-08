import pygame


class Player:
    def __init__(self):

        spawn_x = 165
        spawn_y = 400

        self.sprite = pygame.image.load('SpaceShip2.png')
        self.rect = self.sprite.get_rect(x=spawn_x, y=spawn_y)
        self.pos = self.sprite.get_locks()

        self.speed = 10
        self.velocity = [0,0]

    def move(self):
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

    def draw(self, surface):
        surface.blit(self.sprite, self.rect)