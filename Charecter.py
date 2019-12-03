import pygame


class Charecter:
    def __init__(self, img, pos_x, pos_y):
        self._image = img
        self._pos_x = pos_x
        self._pos_y = pos_y

    def get_image(self):
        return self._image

    def get_pos_x(self):
        return self._pos_x

    def get_pos_y(self):
        return self._pos_y

    def set_pos_x(self, x):
        self._pos_x = x

    def set_pos_y(self, y):
        self._pos_y = y

    def get_width(self):
        return self.get_image().get_size()[0]

    def get_height(self):
        return self.get_image().get_size()[1]


