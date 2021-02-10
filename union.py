import itertools
from PIL import Image
import uuid

def union(width: int, height: int, black_and_white: bool = False):
    for c in itertools.product(itertools.product(range(256) if black_and_white else range(0, 256, 255), repeat=3), repeat=(width * height)):
        c = c[::-1]

        img = Image.new('RGB', (width, height))
        _map = img.load()

        for x in range(width):
            for y in range(height):
                _map[x, y] = c[y + width * x]

        yield img
