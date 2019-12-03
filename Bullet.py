import pygame


def increase_bullit():
    Bullet.bullit_count += 1

def decrease_bullit():
    Bullet.bullit_count -= 1


class Bullet:
    bullit_count = 1

    def __init__(self, pos_x, pos_y, velocity=4):
        self._pos_x = pos_x
        self._pos_y = pos_y
        self._size = 40
        self._velocity = velocity
        self._state = False
        self._UID = Bullet.bullit_count
        Bullet.bullit_count += 1
        if Bullet.bullit_count > 3:
            Bullet.bullit_count = 1

    def get_size(self):
        return self._size

    def get_UID(self):
        return self._UID

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state

    def get_pos_x(self):
        return self._pos_x

    def get_pos_y(self):
        return self._pos_y

    def set_pos_x(self, x):
        self._pos_x = x

    def set_pos_y(self, y):
        self._pos_y = y

    def get_velocity(self):
        return self._velocity

    def move_up(self):
        self.set_pos_y(self.get_pos_y() - self.get_velocity())

    def draw_bullet(self, screen, pos_x, pos_y):
        image = pygame.image.load('bullet.png')
        image = pygame.transform.scale(image, (self.get_size(), self.get_size()))
        screen.blit(image, (pos_x, pos_y))
