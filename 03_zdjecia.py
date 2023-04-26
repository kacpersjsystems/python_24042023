from os import walk, path


def find_photos_in_dir(target: str) -> list:
    EXTENSIONS = ('.jpg', '.jpeg', '.png')

    photos = []
    for source, _, files in walk(target):
        photos.extend([path.join(source, file) for file in files if file.endswith(EXTENSIONS)])

    return photos


print(find_photos_in_dir('photos'))
