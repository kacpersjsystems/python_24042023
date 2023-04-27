# from sys import argv
# otrzymujemy wszystko co jest podane po słowie "python"
# w postaci listy
#
# np. python program.py 0 1 2 3
#     ['program.py', '0','1','2','3']

# wenętrzna biblioteka argparse
# zewnętrzna biblioteka click

import argparse

program = argparse.ArgumentParser(prog='Add two numbers')
program.add_argument('--a', type=int, required=True)
program.add_argument('--b', type=int, required=True)
args = program.parse_args()

print(args.a, args.b, args.a + args.b)

