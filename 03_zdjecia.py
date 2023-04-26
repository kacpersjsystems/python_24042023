import argparse
from os import walk, path, makedirs
from PIL import Image
from resizeimage import resizeimage


def find_photos_in_dir(target: str) -> list:
    EXTENSIONS = ('.jpg', '.jpeg', '.png')

    photos = []
    for source, _, files in walk(target):
        photos.extend([path.join(source, file) for file in files if file.endswith(EXTENSIONS)])

    return photos


def resize_image(source: str, target: str):
    with open(source, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [300, 300])
            cover.save(target, image.format)


program = argparse.ArgumentParser(prog='Scale images in specific directory')
program.add_argument('--source', required=True)
program.add_argument('--destination', required=True)
args = program.parse_args()


if not path.exists(args.destination):
    makedirs(args.destination)

for photo in find_photos_in_dir(args.source):
    thumbnail = photo.replace(args.source, args.destination)
    print(photo, ' => ', thumbnail)
    resize_image(photo, thumbnail)

