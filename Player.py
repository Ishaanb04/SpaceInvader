import pygame
from Charecter import Charecter
from Bullet import Bullet


class Player(Charecter):
    def __init__(self, image, pos_x, pos_y, velocity=7):
        super().__init__(image, pos_x, pos_y)
        self._bullets = []
        self._velocity = velocity

    def get_bullets(self):
        return self._bullets

    def create_bullet(self):
        bullet = Bullet(self.get_pos_x(), self.get_pos_y())
        bullet.set_pos_x(self.get_pos_x() + bullet.get_size() // 2 - 7.5)
        bullet.set_pos_y(self.get_pos_y() - 30)
        self.get_bullets().append(bullet)

    def get_velocity(self):
        return self._velocity

    def create_player(self, screen):
        screen.blit(self.get_image(), (self.get_pos_x(), self.get_pos_y()))

    def move_left(self):
        self.set_pos_x(self.get_pos_x() - self.get_velocity())

    def move_right(self):
        self.set_pos_x(self.get_pos_x() + self.get_velocity())

    def move_up(self):
        self.set_pos_y(self.get_pos_y() - self.get_velocity())

    def move_down(self):
        self.set_pos_y(self.get_pos_y() + self.get_velocity())