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
parser.add_argument('-p', '--part', help='part to run', default=['1','2'])

args = parser.parse_args()
day = args.day or datetime.date.today().day
file = args.file or f'in/day{day:0>2}.txt'
part = args.part if type(args.part) == list else [args.part]


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


code = importlib.import_module(f'.days.day{day:0>2}', 'src')

with open(file, 'r') as f:
    data = f.read()

    for p in part:
        t0 = time.process_time_ns()
        fn = getattr(code, f'part{p}', None)
        if fn:
            ret = fn(data)
            el = time.process_time_ns() - t0
            print(f'Part {p}: {ret} in {el/1e6} ms')
