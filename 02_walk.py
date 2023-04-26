# os - operating system
from os import walk

for path, directories, files in walk('.'):
    if 'venv' in path:
        # jeżeli venv znajduje się w path to przejdź do kolejnego pliku
        continue

    print(path, 'ilość plików', len(files))
    for file in files:
        if file.endswith('.py'):
            print(path, file)
