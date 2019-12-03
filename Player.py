import pygame
from Charecter import Charecter
from Bullet import Bullet
from MyQueue import Queues

class Player(Charecter):
    def __init__(self, image, pos_x, pos_y, velocity = 7):
        super().__init__(image, pos_x, pos_y)
        self._max_bullets = 3
        self._bullets = Queues(self._max_bullets)
        self._velocity = velocity

    def get_max_bullets(self):
        return self._max_bullets

    def get_bullets(self):
        return self._bullets

    def create_bullet(self):
        bullet = Bullet(self.get_pos_x(), self.get_pos_y())
        self.get_bullets().enqueue(bullet)

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