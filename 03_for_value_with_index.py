word = 'Python'

# domyślnie start=0, ale możemy to zmodyfikować
for position, char in enumerate(word, start=1):
    print(f'Znak {char} znajduje się na pozycji {position}.')


