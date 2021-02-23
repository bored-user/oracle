import argparse
import os
import sys
import uuid

import utils
import oracle


def parse_args():
    abspath = os.path.abspath(os.path.dirname(__file__))

    parser = argparse.ArgumentParser(
        description='Generate all possible image combinations using a given width and height', prog='Oracle')
    parser.add_argument('-s', '--size', required=True, type=int,
                        nargs=2, help='Width and height of images (in pixels)')
    parser.add_argument('-p', '--path', default=f'{abspath}/images', required=False, type=str,
                        help=f'Path where the images will be saved (defaults to {abspath}/images)')
    parser.add_argument('---estimate-size', action='store_true',
                        help='Prints the estimated size of (all) images and exit.')
    parser.add_argument('---estimate-ammount', action='store_true',
                        help='Prints the total number of images that would be generated and exit.')
    parser.add_argument('-e', '--estimate', action='store_true', help='Alias to ---estimate-size ---estimate-ammount')
    parser.add_argument('---black-white', action='store_true',
                        help='If given, all images will be black and white (RGB 0,0,0 and 255,255,255)')

    return parser.parse_args()


def main() -> int:
    args = parse_args()
    args.path += '/' if args.path[-1] != '/' else ''
    size = utils.estimate_size(args.size[0], args.size[1], args.path, args.black_white)
    ammount = utils.ammount_of_images(args.size[0] * args.size[1], args.black_white)

    if not os.path.isdir(args.path):
        os.makedirs(args.path)

    if args.estimate: return print(f'{ammount} images\n{size}') or 0
    if args.estimate_size: return print(size) or 0
    if args.estimate_ammount: return print(f'{ammount} images') or 0

    [ img.save(f'{args.path}{uuid.uuid4()}.jpg') for img in oracle.oracle(args.size[0], args.size[1], args.black_white) ]
    return 0


if __name__ == '__main__':
    sys.exit(main())
