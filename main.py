# -*- coding: utf-8 -*-
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sbn

from ForestGrid import Forest

sbn.set_theme(style="dark")

AREA = 100
grid = Forest(AREA)
grid.init()


def update(loop: int):
    global grid
    COLORS = ['red', 'grey', 'green']
    CMAP = mpl.colors.ListedColormap(COLORS)
    EMPTY = [0]
    NORMAL = [AREA ** 2]
    ONFIRE = [0]

    plt.ion()
    plt.figure(figsize=(7, 7))

    for time in range(loop):
        plt.imshow([[tree.state for tree in row] for row in grid.matrix], cmap=CMAP)

        EMPTY.append(len(np.where(np.vectorize(lambda tree: tree.is_empty())(grid.matrix))[0]))
        NORMAL.append(len(np.where(np.vectorize(lambda tree: tree.is_normal())(grid.matrix))[0]))
        ONFIRE.append(len(np.where(np.vectorize(lambda tree: tree.is_on_fire())(grid.matrix))[0]))

        # update
        grid.update()

        if time <= 10:
            plt.pause(0.5)

    plt.ioff()

    plt.figure(7, figsize=(19.20, 9.61))
    t = [i for i in range(loop + 1)]

    plt.plot(t, EMPTY, label='Vacancy', lw=2, color=(165 / 255, 165 / 255, 165 / 255))
    plt.plot(t, NORMAL, label='Trees', lw=2, color=(28 / 255, 172 / 255, 76 / 255))
    plt.plot(t, ONFIRE, label='Burning', lw=2, color=(239 / 255, 29 / 255, 31 / 255))

    plt.grid(linestyle=":")
    plt.legend()

    plt.show()


if __name__ == '__main__':
    update(100)
    plt.figure(figsize=(19.20, 9.61))
    sbn.heatmap([[tree.state for tree in row] for row in grid.matrix],
                cmap=[(239 / 255, 29 / 255, 31 / 255),
                      (165 / 255, 165 / 255, 165 / 255),
                      (28 / 255, 172 / 255, 76 / 255)], annot=True)
    plt.show()
