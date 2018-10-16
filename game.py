from matplotlib import pyplot as plt
from scipy import ndimage
import numpy as np


def rules(x, neighbors):
    """ 
    Evolve every cell in the map according to thee rules:
        - If cell is alive and has 2 or 3 live neighbors -> alive
        - If cell is dead and has 3 live neighbors -> alive
        - Otherwise cell -> dead
    """
    return 1 * (x == 1 and (neighbors == 2 or neighbors == 3) or (x == 0 and (neighbors == 3)))


def live(dim, prob):
    v_rules = np.vectorize(rules)

    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    life = np.random.choice(2, size=(dim, dim), p=[prob, 1-prob])

    while True:
        plt.imshow(life)
        plt.pause(0.1)
        plt.clf()

        neighbors_matrix = ndimage.convolve(life, kernel, mode='constant', cval=0.0)
        life = v_rules(life, neighbors_matrix)

if __name__ == '__main__':
    live(30, 0.4)
