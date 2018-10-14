import random
import numpy as np
from matplotlib import pyplot as plt
from geo_to_cartesian import read_coords
random.seed(365)


def gen_random_coords(n=10, fx=800, fy=800, fr=50):
    coords = []
    for i in range(n):
        a = fx*random.random()
        b = fy*random.random()
        r = fr*random.random()
        coords.append((a,b,r))

    return coords

def gen_grid(fx=800, fy=800, fr=50):
    grid = np.zeros((fx+fr, fy+fr))
    return grid

def color_grid(grid, coords, scale, min_x, min_y):
    # https://stackoverflow.com/questions/8647024/how-to-apply-a-disc-shaped-mask-to-a-numpy-array
    m, n = grid.shape
    for a, b, r in coords:
        print(a, b, r)
        a = int((a-min_x) * scale)
        b = int((b-min_y) * scale)
        r = int(r*scale)
        print(a, b, r)
        y, x = np.ogrid[-a:m-a, -b:n-b]
        mask = x*x + y*y <= r*r
        grid[mask] += 1

def show_as_image(grid):
    plt.gray()
    plt.imshow(grid, interpolation='nearest')
    plt.show()

if __name__ == '__main__':
    coord_vals = read_coords(fname='coords2.txt')
    coords = coord_vals['coords']
    print(coords,)
    max_x, min_x = coord_vals['max_x'], coord_vals['min_x']
    max_y, min_y = coord_vals['max_y'], coord_vals['min_y']
    print(coord_vals['max_long'], coord_vals['min_long'], coord_vals['max_long'] - coord_vals['min_long'])
    print(coord_vals['max_lat'], coord_vals['min_lat'], coord_vals['max_lat'] - coord_vals['min_lat'])
    max_diff = max(max_x - min_x,
                   max_y - min_y)
    grid = gen_grid()
    m, n = grid.shape
    scale = min(m, n) / max_diff
    print(scale)
    color_grid(grid, coords, scale, min_x, min_y)
    show_as_image(grid)

