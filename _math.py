import os
import random
import uuid
from decimal import Decimal

from PIL import Image


def ammount_of_images(area: int) -> int: return 256 ** 3 ** area


def estimate_size(width: int, height: int, path: str) -> str:
    names = [uuid.uuid4(), uuid.uuid4(), uuid.uuid4()]
    imgs = [Image.new('RGB', (width, height)), Image.new('RGB', (width, height)), Image.new('RGB', (width, height))]
    sizes = []

    for i in range(3):
        _map = imgs[i].load()

        for x in range(width):
            for y in range(height):
                _map[x, y] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        _path = f'{path}{names[i]}.jpg'
        imgs[i].save(_path)
        sizes.append(os.stat(_path).st_size)
        os.remove(_path)

    B = Decimal(sum(sizes) / 3 * ammount_of_images(width * height))
    KB = Decimal(1024)
    MB = Decimal(KB ** 2)  # 1,048,576
    GB = Decimal(KB ** 3)  # 1,073,741,824
    TB = Decimal(KB ** 4)  # 1,099,511,627,776
    PB = Decimal(KB ** 5)  # 1,125,899,906,842,624
    EB = Decimal(KB ** 6)  # 1.152921504606847e+18
    ZB = Decimal(KB ** 7)  # 1.1805916207174113e+21
    YB = Decimal(KB ** 8)  # 1.2089258196146292e+24

    if B < KB:
        return '{0:.2f} B'.format(B)
    elif KB <= B < MB:
        return '{0:.2f} KB'.format(B/KB)
    elif MB <= B < GB:
        return '{0:.2f} MB'.format(B/MB)
    elif GB <= B < TB:
        return '{0:.2f} GB'.format(B/GB)
    elif TB <= B < PB:
        return '{0:.2f} TB'.format(B/TB)
    elif PB <= B < TB:
        return '{0:.2f} PB'.format(B/PB)
    elif EB <= B < PB:
        return '{0:.2f} EB'.format(B/EB)
    elif ZB <= B < EB:
        return '{0:.2f} ZB'.format(B/ZB)
    else:
        return '{0:.2f} YB'.format(B/YB)
