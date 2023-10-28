# -*- coding: utf-8 -*-
import random


# Cellular
class Tree(object):
    """
    Tree has three state: empty(0), normal(1), on fire(-1)
    growth_p : float
        probability of tree growth.
    fire_p : float
        probability of a tree being ignited.
    """

    def __init__(self, coordinate_x, coordinate_y):
        self.state = 1
        self.coordinate = [coordinate_x, coordinate_y]
        self.growth_p = 0.25
        self.fire_p = 0.01

    def growth(self):
        if random.random() < self.growth_p:
            self.state = 1

    def random_fire(self):
        if random.random() < self.fire_p:
            self.fire()

    def fire(self):
        self.state = -1

    def destroy(self):
        self.state = 0

    def is_empty(self):
        return self.state == 0

    def is_normal(self):
        return self.state == 1

    def is_on_fire(self):
        return self.state == -1

    def growth_p(self, p):
        self.growth_p = p

    def fire_p(self, p):
        self.fire_p = p
