#!/bin/python3

import argparse
import datetime
import importlib
import time
import os
import sys

parser = argparse.ArgumentParser('AoC23')
parser.add_argument('-d', '--day', help='day number to run, or empty for today')
parser.add_argument('-f', '--file', help='file with puzzle input, or empty for default')

args = parser.parse_args()
day = args.day or datetime.date.today().day
file = args.file or f'in/day{day:02}.txt'


'''
# Requires session for personal input
if not os.path.isfile(file):
    import requests
    print('Puzzle input not found, downloading...')

    res = requests.get(f'https://adventofcode.com/2023/day/{day}/input')

    if res.text.startswith('Please'):
        print(f'You are too early for day {day}!')
        sys.exit(0)

    with open(file, 'w') as f:
        f.write(res.text)
'''


code = importlib.import_module(f'.days.day{day:02}', 'src')

with open(file, 'r') as f:
    data = f.read()

    t0 = time.process_time_ns()
    ret = code.part1(data)
    el = time.process_time_ns() - t0
    print(f'Part 1: {ret} in {el/1e3} ms')

    if hasattr(code, 'part2'):
        t0 = time.process_time_ns()
        code.part2(data)
        el = time.process_time_ns() - t0
        print(f'Part 2: {ret} in {el/1e3} ms')
