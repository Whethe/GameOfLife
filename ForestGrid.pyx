import cython
import numpy as np

from Tree import Tree


class Forest(object):
    def __init__(self, area):
        self.matrix = None
        self.area = area
        self.neighbors = [(0, 1),
                          (1, 0),
                          (-1, 0),
                          (0, -1)]
        self.origin = True

    def init(self):
        self.matrix = np.empty([self.area, self.area], dtype=object)
        for i in range(self.area):
            for j in range(self.area):
                self.matrix[i, j] = Tree(i, j)

    def update(self):
        _matrix = self.matrix
        fire_tree = [(i, j) for i in range(self.area) for j in range(self.area) if _matrix[i, j].is_on_fire()]

        # Spreading the fire, update state in next loop
        for i, j in fire_tree:
            for dx, dy in self.neighbors:
                # Calculate neighbor coordinates
                x, y = i + dx, j + dy
                # Filter out invalid coordinates
                # Check if the neighbor is within bounds
                if 0 <= x < self.area and 0 <= y < self.area:
                    neighbor_tree = _matrix[x, y]
                    if neighbor_tree.is_normal():
                        neighbor_tree.fire()

        # Let trees growth in next state
        # Randomly set some tree on fire to simulate real life accident
        for i in range(self.area):
            for j in range(self.area):
                tree = _matrix[i, j]

                if tree.is_normal():
                    tree.random_fire()

                if tree.is_empty():
                    tree.growth()
        self.origin = False

        # Set previously on fire trees to empty
        for i, j in fire_tree:
            _matrix[i, j].destroy()
