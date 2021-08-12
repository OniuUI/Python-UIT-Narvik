'''
#
# Obligatorisk karaktersatt oppgave #1
#
# Legg spesielt merke til at det er kun koden i klassen Kalman som kan endres. Det er koden som skal leveres inn
# Det er derfor viktig at INGEN ANNEN KODE ENDRES !!!
#
'''
from typing import Any, Union

import pygame as pg
from random import random, randint
import numpy as np
from numpy.linalg import norm

fps = 0.0


class Projectile():

    def __init__(self, background, kalman=None):
        self.background = background
        self.rect = pg.Rect((800, 700), (16, 16))
        self.px = self.rect.x
        self.py = self.rect.y
        self.dx = 0.0
        self.kalm = kalman

    def move(self, goal):

        if self.kalm:
            goal = self.kalm.calc_next(goal)

        deltax = np.array(float(goal) - self.px)
        # print(delta2)
        mag_delta = norm(deltax)  # * 500.0
        np.divide(deltax, mag_delta, deltax)

        self.dx += deltax
        # if self.dx:
        # self.dx /= norm(self.dx) * 50

        self.px += self.dx / 50.0
        self.py += -0.5
        try:
            self.rect.x = int(self.px)
        except:
            pass
        try:
            self.rect.y = int(self.py)
        except:
            pass


class Target():

    def __init__(self, background, width):
        self.background = background
        self.rect = pg.Rect(self.background.get_width() // 2 - width // 2,
                            50, width, 32)
        self.dx = 1 if random() > 0.5 else -1

    def move(self):
        self.rect.x += self.dx

        if self.rect.x < 300 or self.rect.x > self.background.get_width() - 300:
            self.dx *= -1

    def noisy_x_pos(self):
        pos = self.rect.x
        center = self.rect.width // 2
        noise = np.random.normal(0, 1, 1)[0]

        return pos + center + noise * 300.0


#
# Her er Kalmanfilteret du skal utvikle
#
class Kalman():

    def __init__(self):
        self._xn_n = 0
        self._xn_n_minus_1 = 0
        self._xn_n_plus_1 = 0
        self._x_dot_n_n = 0
        self._x_dot_n_minus_1 = 0
        self._d_t = 5
        self.alpha = 0.23
        self.beta = 0.395

    def calc_next(self, zi):

        # _xn_n_minus_1 at N - 1
            self._xn_n_minus_1 = self._xn_n_plus_1

        # State Update Equation for position
            self._xn_n = self._xn_n_minus_1 + self.alpha * (zi - self._xn_n_minus_1)

        # State Update Equation for velocity
            self._x_dot_n_n = self._x_dot_n_minus_1 + self.beta * ((zi - self._xn_n_minus_1) / self._d_t)

        # Estimate uncertainty extrapolation
            self._xn_n_plus_1 = self._xn_n + self._d_t * self._x_dot_n_n

            return self._xn_n_plus_1


pg.init()

w, h = 1600, 800

background = pg.display.set_mode((w, h))
surf = pg.surfarray.pixels3d(background)
running = True
clock = pg.time.Clock()

kalman_score = 0
reg_score = 0
iters = 0

while running:
    target = Target(background, 32)
    missile = Projectile(background)
    k_miss = Projectile(background, Kalman())  # kommenter inn denne linjen naar Kalman er implementert
    last_x_pos = target.noisy_x_pos
    noisy_draw = np.zeros((w, 20))

    trial = True
    iters += 1

    while trial:

        # Setter en maksimal framerate på 300. Hvis dere vil øke denne er dette en mulig endring
        clock.tick(300)
        fps = clock.get_fps()

        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False

        background.fill(0x448844)
        surf[:, 0:20, 0] = noisy_draw

        last_x_pos = target.noisy_x_pos()

        #print(last_x_pos)

        target.move()
        missile.move(last_x_pos)
        k_miss.move(last_x_pos)  # kommenter inn denne linjen naar Kalman er implementert

        pg.draw.rect(background, (255, 200, 0), missile.rect)
        pg.draw.rect(background, (0, 200, 255), k_miss.rect)  # kommenter inn denne linjen naar Kalman er implementert
        pg.draw.rect(background, (255, 200, 255), target.rect)

        noisy_draw[int(last_x_pos):int(last_x_pos) + 20, :] = 255
        noisy_draw -= 1
        np.clip(noisy_draw, 0, 255, noisy_draw)

        coll = missile.rect.colliderect(target.rect)
        k_coll = k_miss.rect.colliderect(target.rect)  # kommenter inn denne linjen naar Kalman er implementert#

        if coll:
            reg_score += 1

        if k_coll:  # kommenter inn denne linjen naar Kalman er implementert
            kalman_score += 1

        oob = missile.rect.y < 20

        if oob or coll or k_coll:  # endre denne sjekken slik at k_coll ogsaa er med naar kalman er implementert
            trial = False

        pg.display.flip()

    print('kalman score: ', round(kalman_score / iters, 2))  # kommenter inn denne linjen naar Kalman er implementert
    print('regular score: ', round(reg_score / iters, 2))

pg.quit()
