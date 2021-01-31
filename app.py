import argparse
import itertools
import os
import sys
import uuid

from PIL import Image

import _math

ABSPATH = os.path.abspath(os.path.dirname(__file__))


def parse_args():
    parser = argparse.ArgumentParser(
        description='Generate all possible image combinations using a given width and height')
    parser.add_argument('-s', '--size', required=True, type=int,
                        nargs=2, help='Width and height of images (in pixels)')
    parser.add_argument('-p', '--path', default=f'{ABSPATH}/images', required=False, type=str,
                        help=f'Path where the images will be saved (defaults to {ABSPATH}/images)')
    parser.add_argument('---estimate-only', default=False, required=False, nargs='?',
                        help='Prints the estimated size of (all) images and exit.')
    parser.add_argument('---ammount-only', default=False, required=False, nargs='?',
                        help='Prints the total number of images that would be generated and exit.')
    parser.add_argument('---black-white', default=False, required=False, nargs='?', help='If given, all images will be black and white (RGB 0,0,0 and 255,255,255)')

    args = parser.parse_args()

    return args.size, args.path, args.estimate_only, args.ammount_only, args.black_white


def main() -> int:

    [width, height], path, estimate_only, ammount_only, black_white = parse_args()
    path += '/' if path[-1] != '/' else ''

    if not os.path.isdir(path):
        os.makedirs(path)

    if estimate_only != False:
        print(_math.estimate_size(width, height, path, black_white == None))
        return 0

    if ammount_only != False:
        print(f'{_math.ammount_of_images(width * height, black_white == None)} images')
        return 0

    for color in itertools.product(itertools.product(range(256) if black_white != None else range(0, 256, 255), repeat=3), repeat=(width * height)):
        color = color[::-1]

        img = Image.new('RGB', (width, height))
        _map = img.load()

        for x in range(width):
            for y in range(height):
                _map[x, y] = color[y + width * x]

        img.save(f"{path}{uuid.uuid4()}.jpg")

    return 0


if __name__ == '__main__':
    sys.exit(main())
