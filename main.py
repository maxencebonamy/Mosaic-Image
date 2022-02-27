import PIL.Image
import scipy.spatial
import numpy as np
import sys
import os

from config import *


class LoadingBar:

    def __init__(self, name, maximum):
        self.maximum = maximum
        self.value = 0
        print(name)

    def print(self):
        percent = round(self.value / self.maximum * 100)
        print(f"\r|{'█' * percent}{' ' * (100 - percent)}| {percent}%", end="")

    def increment(self):
        if self.value < self.maximum:
            self.value += 1

    def __del__(self):
        print("\n")


def load_tile_set():
    TILE_SET_PATH = os.path.join("tile_set", TILE_SET)

    tiles = []
    colors = []
    images = [os.path.join(TILE_SET_PATH, file) for file in os.listdir(TILE_SET_PATH)]

    loading_bar = LoadingBar(">>> TILE SET LOADING...", len(images))
    for path in images:
        try:
            tile = PIL.Image.open(path).resize(TILE_SIZE.tuple())
            tiles.append(tile)
            colors.append(np.array(tile).mean(axis=0).mean(axis=0))
        except:
            pass
        loading_bar.print()
        loading_bar.increment()
    del loading_bar

    return tiles, colors


def convert(image_name):
    image_path = os.path.join("input", image_name)

    image = PIL.Image.open(image_path)
    size = Vect(*image.size)

    new_size = round(Vect(*image.size) / COMPRESSION_RATE)
    new_image = image.resize(new_size.tuple())

    tree = scipy.spatial.KDTree(colors)

    output_image = PIL.Image.new('RGB', round(size * TILE_SIZE / COMPRESSION_RATE).tuple())

    loading_bar = LoadingBar(">>> IMAGE GENERATING...", new_size.x * new_size.y)
    for i in range(new_size.x):
        for j in range(new_size.y):
            index = Vect(i, j)

            closest = tree.query(new_image.getpixel(index.tuple()))
            position = index * TILE_SIZE
            output_image.paste(tiles[closest[1]], position.tuple())

            loading_bar.print()
            loading_bar.increment()
    del loading_bar

    # Save output
    output_image.save(os.path.join("output", image_name))
    print(">>> IMAGE SAVED")


if __name__ == '__main__':
    tiles, colors = load_tile_set()
    convert(IMAGE_NAME)