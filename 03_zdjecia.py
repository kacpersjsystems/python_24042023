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





if not path.exists('thumbnails'):
    makedirs('thumbnails')

for photo in find_photos_in_dir('photos'):
    thumbnail = photo.replace('photos', 'thumbnails')
    print(photo, ' => ', thumbnail)
    resize_image(photo, thumbnail)

