example = '''Time:      7  15   30
Distance:  9  40  200'''

import re
import numpy as np
import functools


def solve(t0, d):
    tc = np.arange(0, t0+1)
    x = tc * (t0 - tc)
    return sum(x > d)

def part1(data):
    pat = re.compile(r'\d+')
    pairs = zip(*map(
        lambda x: list(map(int, pat.findall(x))),
        data.splitlines()))

    return functools.reduce(lambda x,y: x*solve(*y), pairs, 1)

def part2(data):
    p = map(lambda x: int(x.split(':')[1]), data.replace(' ', '').splitlines())
    return solve(*p)
