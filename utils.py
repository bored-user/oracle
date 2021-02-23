import os
import random
import uuid

from PIL import Image
from decimal import Decimal

import conversor


def ammount_of_images(area: int, bw: bool) -> int: return (16777216 if not bw else 2) ** area


def estimate_size(width: int, height: int, path: str, bw: bool) -> str:
    names = [uuid.uuid4() for _ in range(3)]
    imgs = [Image.new('RGB', (width, height)) for _ in range(3)]
    sizes = []

    for i in range(3):
        img = imgs[i].load()

        for x in range(width):
            for y in range(height):
                img[x, y] = tuple(random.randint(0, 255) for _ in range(3)) if not bw else random.choice([(0, 0, 0), (255, 255, 255)])

        _path = f'{path}{names[i]}.jpg'
        imgs[i].save(_path)
        sizes.append(os.stat(_path).st_size)
        os.remove(_path)

    return conversor.to_readable(Decimal(sum(sizes)) / Decimal(3) * Decimal(ammount_of_images(width * height, bw)))
