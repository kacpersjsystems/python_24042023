from string import ascii_uppercase, ascii_lowercase
from random import shuffle, choices

print(list(ascii_lowercase))
small_letters = choices(list(ascii_lowercase), 5)
big_letters = choices(list(ascii_uppercase), 5)
numbers = choices(range(10), 3)
password = ['%', '@', '!', '&'] + small_letters + big_letters + numbers

print(shuffle(password))

