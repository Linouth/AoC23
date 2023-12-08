example = '''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
'''

import math
from functools import reduce


def part1(data):
    lines = data.splitlines()
    dirs = [ 0 if x=='L' else 1 for x in lines[0] ]
    maps = { line[0:3] : (line[7:10], line[12:15]) for line in lines[2:] }

    state = 'AAA'
    steps = 0
    while state != 'ZZZ':
        state = maps[state][dirs[steps % len(dirs)]]
        steps += 1

    return steps


def part2(data):
    lines = data.splitlines()
    dirs = [ 0 if x=='L' else 1 for x in lines[0] ]
    maps = { line[0:3] : (line[7:10], line[12:15]) for line in lines[2:] }

    start = [ k for k in maps.keys() if k[2]=='A' ]

    taken = []
    for state in start:
        steps = 0
        while state[2] != 'Z':
            state = maps[state][dirs[steps % len(dirs)]]
            steps += 1
        taken.append(steps)

    return reduce(lambda a,b: a*b//math.gcd(a,b), taken)
