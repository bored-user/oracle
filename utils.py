import os
import random
import uuid

from PIL import Image
import conversor

def ammount_of_images(
    area: int, bw: bool) -> int: return ((256 if not bw else 2) ** 3) ** area


def estimate_size(width: int, height: int, path: str, bw: bool) -> str:
    names = [uuid.uuid4(), uuid.uuid4(), uuid.uuid4()]
    imgs = [Image.new('RGB', (width, height)), Image.new(
        'RGB', (width, height)), Image.new('RGB', (width, height))]
    sizes = []

    for i in range(3):
        _map = imgs[i].load()

        for x in range(width):
            for y in range(height):
                _map[x, y] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) if not bw else (
                    random.choices([0, 255])[0], random.choices([0, 255])[0], random.choices([0, 255])[0])

        _path = f'{path}{names[i]}.jpg'
        imgs[i].save(_path)
        sizes.append(os.stat(_path).st_size)
        os.remove(_path)

    return conversor.to_readable((sum(sizes) / 3) * ammount_of_images(width * height, bw))
