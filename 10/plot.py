from typing import List
import matplotlib.pyplot as plt

plot_id = 0
# plt.gca().invert_yaxis()


def plot(x_coordinates: List[int], y_coordinates: List[int]):
    plt.clf()
    plt.gca().invert_yaxis()
    plt.plot(x_coordinates, y_coordinates, 'ro')
    global plot_id
    plot_id += 1
    name = "plots/plot_" + str(plot_id) + ".png"
    plt.savefig(name, bbox_inches='tight')