import pygame
import random
from Player import Player
from Enemy import Enemy


class MainGame:
    CLOCK = pygame.time.Clock()

    def __init__(self, is_running=False, width=1280, height=720, max_enemy=3, max_bullets=3):
        pygame.init()
        self._screen_width = width
        self._screen_height = height
        self._screen = self.screen_setup()
        self._is_running = is_running
        self._player = self.create_player()
        self._enemy = []
        self._max_enemy = max_enemy
        self._bullet_count = 0
        self._max_bullet = max_bullets
        self._score = 0
        self._background = self.back_ground_setup()
        self._is_exit = True
        self.get_screen().blit(self.get_background(), (0, 0))

    def get_max_enemy(self):
        return self._max_enemy

    def is_exit(self):
        return self._is_exit

    def set_is_exit(self, exit_1):
        self._is_exit = exit_1

    def get_background(self):
        return self._background

    def back_ground_setup(self):
        img = pygame.image.load('background.png')
        img = pygame.transform.scale(img, (self.get_screen_width(), self.get_screen_height()))
        return img

    def get_score(self):
        return self._score

    def inc_score(self):
        self._score += 1

    def display_text(self, size):
        font = pygame.font.Font('freesansbold.ttf', size)
        return font

    def get_max_bullet(self):
        return self._max_bullet

    def get_bullet_count(self):
        return self._bullet_count

    def inc_bullet_count(self):
        self._bullet_count += 1

    def dec_bullet_count(self):
        self._bullet_count -= 1

    def create_player(self):
        player_img = pygame.image.load('space-invaders.png')
        player = Player(player_img, 0, 0, 10)
        player.set_pos_x(self.get_screen_width() // 2 - player.get_height() // 2)
        player.set_pos_y(self.get_screen_height() - 100)
        return player

    def get_enemy(self):
        return self._enemy

    def create_enemy(self):
        enemy_image = pygame.image.load('space-enemy.png')
        if len(self.get_enemy()) < self.get_max_enemy():
            enemy = Enemy(enemy_image, random.randint(5, self.get_screen_width() - 5 - enemy_image.get_size()[0]),
                          random.randint(5, self.get_screen_height() // 2 - enemy_image.get_size()[1] // 2))
            self.get_enemy().append(enemy)
        return self.get_enemy()

    def respawn(self, enemy_x, enemy_y):
        enemy_image = pygame.image.load('space-enemy.png')
        for i, en in enumerate(self.get_enemy()):
            if en.get_pos_x() == enemy_x and en.get_pos_y() == enemy_y:
                self.get_enemy()[i] = Enemy(enemy_image,
                                            random.randint(5, self.get_screen_width() - 5 - enemy_image.get_size()[0]),
                                            random.randint(5, self.get_screen_height() // 2 - enemy_image.get_size()[
                                                1] // 2))
        self.display_enemy()

    def display_enemy(self):
        if self.get_enemy():
            for en in self.get_enemy():
                en.move_down()
                en.create_enemy(self.get_screen())

    def get_screen_width(self):
        return self._screen_width

    def get_screen_height(self):
        return self._screen_height

    def get_screen(self):
        return self._screen

    def is_running(self):
        return self._is_running

    def get_player(self):
        return self._player

    def set_is_running(self, running):
        self._is_running = running

    def screen_setup(self):
        screen = pygame.display.set_mode((self.get_screen_width(), self.get_screen_height()))
        pygame.display.set_caption('Space Invader')
        icon = pygame.image.load('ufo.png')
        pygame.display.set_icon(icon)
        return screen

    def main_loop(self):
        player = self.get_player()
        left_pressed = False
        right_pressed = False
        up_pressed = False
        down_pressed = False

        while self.is_running():
            self.get_screen().blit(self.get_background(), (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.set_is_running(False)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        right_pressed = True
                    elif event.key == pygame.K_LEFT:
                        left_pressed = True
                    elif event.key == pygame.K_UP:
                        up_pressed = True
                    elif event.key == pygame.K_DOWN:
                        down_pressed = True
                    elif event.key == pygame.K_SPACE:
                        if len(player.get_bullets()) < self.get_max_bullet():
                            player.create_bullet()
                            self.inc_bullet_count()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        right_pressed = False
                    elif event.key == pygame.K_LEFT:
                        left_pressed = False
                    elif event.key == pygame.K_UP:
                        up_pressed = False
                    elif event.key == pygame.K_DOWN:
                        down_pressed = False

            if left_pressed and player.get_pos_x() - 5 > 0:
                player.move_left()
            elif right_pressed and player.get_pos_x() + player.get_width() + 5 < self.get_screen_width():
                player.move_right()

            if up_pressed and player.get_pos_y() > self.get_screen_height() // 2:
                player.move_up()
            elif down_pressed and player.get_pos_y() < self.get_screen_height() - player.get_width() - 5:
                player.move_down()

            for bullet in player.get_bullets():
                if bullet.get_pos_y() + bullet.get_size() <= 0:
                    self.dec_bullet_count()
                    player.get_bullets().pop(0)
                elif bullet.get_pos_y() + bullet.get_size() > 0:
                    for en in self.get_enemy():
                        if en.get_pos_x() <= bullet.get_pos_x() + bullet.get_size() // 2 <= en.get_pos_x() + \
                                en.get_width() and en.get_pos_y() + en.get_height() >= bullet.get_pos_y():
                            if bullet in player.get_bullets():
                                player.get_bullets().remove(bullet)
                                self.dec_bullet_count()
                                self.inc_score()
                                self.respawn(en.get_pos_x(), en.get_pos_y())

                    bullet.move_up()
                    bullet.draw_bullet(self.get_screen(), bullet.get_pos_x(), bullet.get_pos_y())

            text = self.display_text(15)
            score_text = text.render(f'Score: {self.get_score()}-Bullet left: '
                                     f'{self.get_max_bullet() - self.get_bullet_count()}', 1, (255, 255, 255))
            self.get_screen().blit(score_text, (5, 5))
            self.create_enemy()
            self.display_enemy()
            self.get_player().create_player(self.get_screen())
            pygame.display.update()

            for en in self.get_enemy():
                if en.get_pos_y() + en.get_height() >= self.get_screen_height():
                    self.set_is_running(False)
                    val = self.second_loop()
                    if val and val[0] and not val[1]:
                        restart_game = MainGame(True, max_enemy=self.get_max_enemy(), max_bullets=self.get_max_bullet())
                        del self
                        restart_game.main_loop()
                if en.get_pos_x() <= player.get_pos_x() + player.get_width() // 2 <= en.get_pos_x() + en.get_width() \
                        and en.get_pos_y() + en.get_height() >= player.get_pos_y():
                    self.set_is_running(False)
                    val = self.second_loop()
                    if val and val[0] and not val[1]:
                        restart_game = MainGame(True, max_enemy=self.get_max_enemy(), max_bullets=self.get_max_bullet())
                        del self
                        restart_game.main_loop()

    def second_loop(self):
        while self.is_exit():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.set_is_exit(False)

                if event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_SPACE:
                        self.set_is_running(True)
                        self.set_is_exit(False)
                        return [self.is_running(), self.is_exit()]
            self.get_screen().blit(self.get_background(), (0, 0))
            text = self.display_text(70)
            restart_text = self.display_text(50)

            score_text = text.render(f'Score: {self.get_score()}', 1, (255, 255, 255))
            restart = restart_text.render('SPACE TO RESTART', 1, (255, 255, 255))
            self.get_screen().blit(score_text, (self.get_screen_width() // 2 - score_text.get_width() // 2, self.get_screen_height() // 2 - score_text.get_height() // 2))
            self.get_screen().blit(restart, (self.get_screen_width() // 2 - restart.get_width() // 2, self.get_screen_height() // 2 + 200))
            pygame.display.update()


if __name__ == '__main__':
    game1 = MainGame(True, max_enemy=5, max_bullets=4)
    game1.main_loop()

