import pygame

import enemys
import player

#dimension
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

#color
BLACK = (0,0,0)
WHITE = (255,255,255)

class Game:
    #Fonction initiant les donnés du jeu
    def __init__(self, surface):
        self.surface = surface

        self.running = True
        self.play = False

        self.run_game = False
        self.nb_run_game = 0

        self.clock = pygame.time.Clock()

        self.tick = pygame.time.get_ticks()
        self.seconds = 0

        self.zone = pygame.Rect(0,0,SCREEN_HEIGHT, SCREEN_WIDTH)

        self.player = player.Player()
        self.asteroid = enemys.Asteroid()

    #Fonction gérant les events
    def handling_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.asteroid.asteroid_y = 0
                    self.asteroid.pos_asteroid = self.asteroid.asteroid.get_rect(x=self.asteroid.asteroid_x,y=self.asteroid.asteroid_y)
                    self.seconds = 0
                    self.run_game = True

            keys = pygame.key.get_pressed()
            # Axe verticale(y)
            if keys[pygame.K_z] or keys[pygame.K_UP]:
                self.player.velocity[1] = -1
            elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
                self.player.velocity[1] = 1
            else :
                self.player.velocity[1] = 0

            # Axe horizontale(x)
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.player.velocity[0] = 1
            elif keys[pygame.K_q] or keys[pygame.K_LEFT]:
                self.player.velocity[0] = -1
            else:
                self.player.velocity[0] = 0

            if keys[pygame.K_ESCAPE]:
                pygame.quit()

    def update(self):
        self.player.move()
        self.asteroid.move()

        if self.asteroid.pos_asteroid.colliderect(self.player.rect):
            self.nb_run_game = 1
            self.run_game = False

    def text(self):
        self.global_font = pygame.font.SysFont('Courier New', 20)

        self.title_font = pygame.font.SysFont('Courier New', 45)
        self.title_text = self.title_font.render('SpaceShooter', 1, WHITE)

        self.begin_font = pygame.font.SysFont('Courier New', 20)
        self.begin_text = self.begin_font.render('Press "enter" for begin', 1, WHITE)

        self.lose_font = pygame.font.SysFont('Courier New', 25)
        self.lose_text = self.lose_font.render(('You had survive :'), 1, WHITE)
        self.lose_text_2 = self.lose_font.render((str(round((self.seconds / 60), 2)) + ' secondes' ), 1, WHITE)

        self.retry_font = pygame.font.SysFont('Courier New', 20)
        self.retry_text = self.retry_font.render('Press "enter" for retry', 1, WHITE)

    def display(self):
        self.surface.fill(BLACK)

        #limite le joueur dans l'écran
        self.player.rect.clamp_ip(self.zone)

        #Dessine les entités
        self.asteroid.draw(self.surface)
        self.player.draw(self.surface)


        pygame.draw.rect(self.surface, BLACK, self.zone, 1)

        if self.run_game == False and self.nb_run_game == 0:
            surface.blit(self.title_text, (40, 200))
            surface.blit(self.begin_text, (60, 350))

        if self.run_game == False and self.nb_run_game > 0:
            surface.blit(self.lose_text, (75, 200))
            surface.blit(self.lose_text_2, (120, 250))
            surface.blit(self.retry_text, (60, 350))
            

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_event()
            self.text()
            self.display()

            if self.run_game == True:
                self.update()

            self.clock.tick(60)
            self.seconds = self.clock.get_time()

pygame.init()
window_icon = pygame.image.load('Astreroïd_2.png')

surface = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
pygame.display.set_caption('SpaceShooter')
pygame.display.set_icon(window_icon)
surface.fill(BLACK)
pygame.display.flip()
launch = Game(surface)
launch.run()

pygame.quit()