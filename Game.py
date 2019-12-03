import pygame
import random
from Player import Player
from Enemy import Enemy
import time
import threading


class MainGame:
    CLOCK = pygame.time.Clock()

    def __init__(self, is_running=False):
        pygame.init()
        self._screen_width = 1000
        self._screen_height = 800
        self._screen = self.screen_setup()
        self._is_running = is_running
        self._player = self.create_player()
        self._enemy = []
        self._bullet_count = 1
        self._max_bullet = 3
        self._score = 0

    def get_score(self):
        return self._score

    def inc_score(self):
        self._score += 1

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
        if len(self.get_enemy()) < 3:
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

    # def bullet_move(self, bullet, player):
    #     collision = False
    #     loc = None
    #     while bullet.get_pos_y() + bullet.get_size() >= 0:
    #         for en in self.get_enemy():
    #             if en.get_pos_x() <= bullet.get_pos_x() + bullet.get_size() // 2 <= en.get_pos_x() + en.get_width() and en.get_pos_y() + en.get_height() >= bullet.get_pos_y():
    #                 print(
    #                     f'Enemy y: {en.get_pos_y() + en.get_height()}, Enemy_x: {en.get_pos_x()} and {en.get_pos_x() + en.get_width()}. Bull_y: {bullet.get_pos_y()} , Bull_x: {bullet.get_pos_x()}')
    #                 collision = True
    #                 loc = [en.get_pos_x(), en.get_pos_y()]
    #                 break
    #         if collision:
    #             player.get_bullets().dequeue()
    #             self.dec_bullet_count()
    #             self.inc_score()
    #             self.respawn(loc[0], loc[1])
    #             time.sleep(1)
    #             break
    #         time.sleep(0.002)
    #         bullet.move_up()
    #         bullet.draw_bullet(self.get_screen(), bullet.get_pos_x(), bullet.get_pos_y())

    def main_loop(self):
        collision = False
        player = self.get_player()
        left_pressed = False
        right_pressed = False
        up_pressed = False
        down_pressed = False
        while self.is_running():
            self.get_screen().fill((0, 0, 0))
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
                        print(f'queue_size{player.get_bullets().get_size()}, max{self.get_max_bullet()}')
                        if player.get_bullets().get_size() <= self.get_max_bullet():
                            print('created')
                            player.create_bullet()
                            self.inc_bullet_count()

                                # else:
                                #     print('bullet_draw')
                                #     bullet.move_up()
                                #     bullet.draw_bullet(self.get_screen(), bullet.get_pos_x(), bullet.get_pos_y())

                        # for bullet in player.get_bullets():
                        #     if bullet.get_pos_y() + bullet.get_size() <= 0:
                        #         self.dec_bullet_count()
                        #         if bullet.get_UID() == 1 and thread1:
                        #             thread1.join()
                        #             player.get_bullets().dequeue()
                        #         elif bullet.get_UID() == 2 and thread2:
                        #             thread2.join()
                        #             player.get_bullets().dequeue()
                        #         elif bullet.get_UID() == 3 and thread3:
                        #             thread3.join()
                        #             player.get_bullets().dequeue()
                        #     else:
                        #         if bullet.get_UID() == 1:
                        #             thread1 = threading.Thread(target=self.bullet_move, args=[bullet, player])
                        #             thread1.start()
                        #         elif bullet.get_UID() == 2:
                        #             thread2 = threading.Thread(target=self.bullet_move, args=[bullet, player])
                        #             thread2.start()
                        #         elif bullet.get_UID() == 3:
                        #             thread3 = threading.Thread(target=self.bullet_move, args=[bullet, player])
                        #             thread3.start()

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
                    print('dequeue1')
                    player.get_bullets().dequeue()
                elif bullet.get_pos_y() + bullet.get_size() > 0:
                    for en in self.get_enemy():
                        if en.get_pos_x() <= bullet.get_pos_x() + bullet.get_size() // 2 <= en.get_pos_x() + en.get_width() and en.get_pos_y() + en.get_height() >= bullet.get_pos_y():
                            print('dequeue2')
                            player.get_bullets().dequeue()
                            self.dec_bullet_count()
                            self.inc_score()
                            self.respawn(en.get_pos_x(), en.get_pos_y())

                    bullet.move_up()
                    bullet.draw_bullet(self.get_screen(), bullet.get_pos_x(), bullet.get_pos_y())

            self.create_enemy()
            self.display_enemy()
            self.get_player().create_player(self.get_screen())
            pygame.display.update()
            MainGame.CLOCK.tick(60)


game1 = MainGame(True)
game1.main_loop()
