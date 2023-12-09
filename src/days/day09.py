example = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
'''
from functools import reduce
from itertools import pairwise


def walk(data, index=-1):
    diff = [ b-a for a,b in pairwise(data) ]

    if any(diff):
        return (*walk(diff, index), diff[index])
    return ()


def part1(data):
    data = [ list(x) for x in [ map(int, line.split(' ')) for line in data.splitlines() ] ]

    return sum( d[-1] + sum(walk(d)) for d in data )


def part2(data):
    data = [ list(x) for x in [ map(int, line.split(' ')) for line in data.splitlines() ] ]

    res = [ d[0] - reduce(lambda a,b: b-a, walk(d, 0)) for d in data ]
    return sum(res)
