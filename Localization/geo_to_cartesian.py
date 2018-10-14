import sys
from math import cos


def equirectangular(L, L0, phi, phi0):
    return (L-L0)*cos(phi0), phi-phi0

def read_coords(fname='coords.txt', fx=1, fy=1, fr=1):
    coords = []
    max_long, min_long = -sys.maxsize, sys.maxsize
    max_lat, min_lat = -sys.maxsize, sys.maxsize
    with open(fname, 'r') as file:
        for line in file:
            lat, long = line.replace('"', '').strip().split('\t')
            long = fx*float(long)
            lat = fy*float(lat)
            r = fr*0.01
            max_long = max(long+r, max_long)
            min_long = min(long-r, min_long)
            max_lat = max(lat+r, max_lat)
            min_lat = min(lat-r, min_lat)
            coords.append([long, lat, None])

    L0 = (max_long + min_long) / 2
    phi0 = (max_lat + min_lat) / 2

    # print(coords)
    max_x, min_x = -sys.maxsize, sys.maxsize
    max_y, min_y = -sys.maxsize, sys.maxsize
    for i, (long, lat, r) in enumerate(coords):
        x, y = equirectangular(long, L0, lat, phi0)
        r = fr*0.01
        coords[i][0] = x
        coords[i][1] = y
        coords[i][2] = r

        max_x = max(x + r, max_x)
        min_x = min(x - r, min_x)
        max_y = max(y + r, max_y)
        min_y = min(y - r, min_y)
    # print(coords)

    coord_vals = {
        'coords': coords,
        'L0': L0,
        'phi0': phi0,
        'max_long': max_long,
        'max_lat': max_lat,
        'min_long': min_long,
        'min_lat': min_lat,
        'max_x': max_x,
        'min_x': min_x,
        'max_y': max_y,
        'min_y': min_y
    }

    return coord_vals

if __name__ == '__main__':
    read_coords()
