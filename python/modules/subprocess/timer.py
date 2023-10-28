#!/usr/bin/python3

# timer.py

from argparse import ArgumentParser
from time import sleep

parser = ArgumentParser()
parser.add_argument("time", type=int)
parser.add_argument("name", type=str)
args = parser.parse_args()
print(f'{args=} ', end=args.name+'\n')
print(f"Starting timer of {args.time} seconds")
for _ in range(args.time):
    print(".", end="pppppp\n", flush=True)
    sleep(1)
print("Done!")

