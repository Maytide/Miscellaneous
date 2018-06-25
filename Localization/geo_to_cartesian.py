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
            long, lat = line.replace('"', '').strip().split('\t')
            long = fx*float(long)
            lat = fy*float(lat)
            max_long = max(long, max_long)
            min_long = min(long, min_long)
            max_lat = max(lat, max_lat)
            min_lat = min(lat, min_lat)
            r = fr*0.01
            coords.append([long, lat, r])

    L0 = (max_long + min_long) / 2
    phi0 = (max_lat + min_lat) / 2

    # print(coords)
    for i, (long, lat, r) in enumerate(coords):
        long, lat = equirectangular(long, L0, lat, phi0)
        coords[i][0] = long
        coords[i][1] = lat
    # print(coords)

    coord_vals = {
        'coords': coords,
        'L0': L0,
        'phi0': phi0,
        'max_long': max_long,
        'max_lat': max_lat,
        'min_long': min_long,
        'min_lat': min_lat
    }

    return coord_vals

if __name__ == '__main__':
    read_coords()
