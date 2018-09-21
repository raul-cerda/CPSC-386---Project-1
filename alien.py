# Raul Cerda
# raul.cerda@csu.fullerton.edu
# Project 1: Alien Invasion

import pygame
import random
from pygame.sprite import Sprite


# uses random num generator to spawn different ships
class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        random_int = random.randint(1,8)
        if random_int < 3:
            self.image = pygame.image.load('images/alien1.png')
        elif random_int < 5:
            self.image = pygame.image.load('images/alien2.png')
        elif random_int < 7:
            self.image = pygame.image.load('images/alien3.png')
        else:
            self.image = pygame.image.load('images/alien4.png')

        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
