example = \
'''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
'''
from collections import namedtuple
import functools
import re

SYMBOLS = {'@', '&', '#', '/', '-', '%', '=', '+', '$', '*'}

Token = namedtuple('Token', ['y', 'x', 'tok'])

@functools.cache
def tokenize(data):
    nums = []
    syms = []

    pat = re.compile(r'(?P<num>\d+)|(?P<sym>[' + re.escape(''.join(SYMBOLS)) + '])')
    for y,line in enumerate(data.splitlines()):
        for match in pat.finditer(line):
            tok = Token(y, match.span()[0], match.group())
            if match.lastgroup == 'num':
                nums.append(tok)
            else:
                syms.append(tok)

    return (nums, syms)
    

def inbounds(n, s):
    return n.x-1 <= s.x <= n.x+len(n.tok) and n.y-1 <= s.y <= n.y+1


def part1(data):
    nums, syms = tokenize(data)

    summation = 0
    for n in nums:
        for s in syms:
            if inbounds(n, s):
                summation += int(n.tok)
                break
    return summation


def part2(data):
    nums, syms = tokenize(data)

    summation = 0
    for s in syms:
        g = -1
        for n in nums:
            if inbounds(n, s):
                if g > -1:
                    summation += g*int(n.tok)
                    break
                else:
                    g = int(n.tok)
    return summation
