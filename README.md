# oracle

Calculate and generate all possible NxN images (where `N` is a user-given integer in pixels).

### Usage

* Required arguments:
    * `-s` (`--size`): Width and height of images (in pixels)

* Optional arguments:
    * `-p` (`--path`): The path where the images will be stored. Defaults to `$PWD/images`
    * `---estimate-size`: If given, will estimate the total size that would've been taken by the images and exit
    * `---estimate-ammount`: If given, will estimate (actually, it's not an estimative) the total ammount of images that would've been generated and exit
    * `---black-white`: If given, will generate only black and white (`rgb(0, 0, 0) and rgb(255, 255, 255)`) images (affects the estimatives as well)

Examples:
```shell
$ python3 app.py -s 1 1 # will generate all 1x1 images possible - that's 256 ^ 3
$ python3 app.py -s 10 10 ---estimate-size # will estimate the ammount taken by all possible 10x10 images (which is 256 ^ 3 ^ 100 images)
$ python3 app.py -s 6 6 ---black-white # will generate all possible 6x6 black and white images (2 ^ 36 images - about 42 TB)
```

### Dependencies

Check `requirements.txt`


### Note on alpha levels (RGBA)

I guess I could've added a way to let the user choose if the script should or should not use RGBA (instead of just the good ol' RGB). But, truth being told, I was lazy xD. Therefore, maybe, in the future, I'll add such feature. Who knows.
