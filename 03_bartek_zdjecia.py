from os import walk, path, makedirs
from PIL import Image
from resizeimage import resizeimage


def find_photos_in_dir(target: str) -> list:
    EXTENSIONS = '.jpg', '.jpeg', '.png'
    photos = []
    for source, _, files in walk(target):
        photos.extend([path.join(source, file) for file in files if file.endswith(EXTENSIONS)])
        # for file in files:
        # if file.endswith(EXTENSIONS):
        # print(path.join(source, file))

    return photos


def resize_image(source: str, target: str):
    with open(source, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [300, 300])
            cover.save(target, image.format)


TARGET_DIRECTORY = 'thumbanils'

if not path.exists(TARGET_DIRECTORY):
    makedirs(TARGET_DIRECTORY)

for photo in find_photos_in_dir('photos'):
    thumbnail = photo.replace('photos', TARGET_DIRECTORY)
    print(photo, ' => ', TARGET_DIRECTORY)
    resize_image(photo, thumbnail)
