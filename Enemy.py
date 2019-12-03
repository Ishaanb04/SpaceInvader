import pygame
from Charecter import Charecter
import time


class Enemy(Charecter):
    def __init__(self, image, pos_x, pos_y, velocity=1):
        super().__init__(image, pos_x, pos_y)
        self._velocity = velocity

    def get_velocity(self):
        return self._velocity

    def move_down(self):
        self.set_pos_y(self.get_pos_y() + self.get_velocity())

    def create_enemy(self, screen):
        screen.blit(self.get_image(), (self.get_pos_x(), self.get_pos_y()))