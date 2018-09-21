# Raul Cerda
# raul.cerda@csu.fullerton.edu
# Project 1: Alien Invasion

import pygame


class Settings:
    # bsse settings shared between every session
    def __init__(self):
        self.screen_width = 1024
        self.screen_height = 576
        self.bg_color = (0, 0, 0)
        self.bg_music = pygame.mixer.Sound('sounds/bg_music.wav')
        self.bg_music.set_volume(0.1)

        self.ship_limit = 3

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    # settings that increase with each level
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        self.fleet_direction = 1

        self.alien_points = 50

    # increases difficulty
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
