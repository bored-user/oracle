import argparse
import os
import sys
import uuid

import utils
import union


def parse_args():
    abspath = os.path.abspath(os.path.dirname(__file__))

    parser = argparse.ArgumentParser(
        description='Generate all possible image combinations using a given width and height')
    parser.add_argument('-s', '--size', required=True, type=int,
                        nargs=2, help='Width and height of images (in pixels)')
    parser.add_argument('-p', '--path', default=f'{abspath}/images', required=False, type=str,
                        help=f'Path where the images will be saved (defaults to {abspath}/images)')
    parser.add_argument('---estimate-size', action='store_true',
                        help='Prints the estimated size of (all) images and exit.')
    parser.add_argument('---estimate-ammount', action='store_true',
                        help='Prints the total number of images that would be generated and exit.')
    parser.add_argument('---black-white', action='store_true',
                        help='If given, all images will be black and white (RGB 0,0,0 and 255,255,255)')

    args = parser.parse_args()

    return args.size, args.path, args.estimate_size, args.estimate_ammount, args.black_white


def main() -> int:
    [width, height], path, estimate_size, estimate_ammount, black_white = parse_args()
    path += '/' if path[-1] != '/' else ''

    if not os.path.isdir(path):
        os.makedirs(path)

    if estimate_size:
        return print(utils.estimate_size(width, height, path, black_white)) or 0

    if estimate_ammount:
        return print(f'{utils.ammount_of_images(width * height, black_white)} images') or 0

    [ img.save(f'{path}{uuid.uuid4()}.jpg') for img in union.union(width, height, black_white) ]
    return 0


if __name__ == '__main__':
    sys.exit(main())
