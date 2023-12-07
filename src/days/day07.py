example = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''

from collections import Counter
from functools import reduce


# Each hand gets a 'score' as follows (each letter represends digits):
# a b c d e    |    ff gg hh ii jj
# abcde are sorted character counts multiplied by [10000 1000 100 10 1]
# respectively (again multiplied by 100**5)
# ffgghhiijj are the scores of each individual card in the order of the input
# These are multiplied by 100**[0, 1, 2, 3, 4]

# Score gen could be extracted into separate function for both part1 and part2


def part1(data):
    hands = [(h, int(i)) for h,i in [x.split(' ') for x in data.splitlines()]]

    SCORES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
              'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    cmp = []
    for h in hands:
        # format abcde
        value_sort = sorted(Counter(h[0]).values(), reverse=True)
        M0 = [10**x for x in range(5)][::-1]
        m0 = sum([ a*b for a,b in zip(value_sort, M0) ])

        # format ffgghhiijj
        M1 = [100**x for x in range(5)][::-1]
        m1 = sum([ SCORES[a]*b for a,b in zip(h[0], M1) ])

        cmp.append((m0 * 100**5 + m1, h[0], h[1]))

    s = sorted(cmp)
    return reduce(lambda a,b: a + b[0]*b[1][2], enumerate(s, start=1), 0)


def part2(data):
    hands = [(h, int(i)) for h,i in [x.split(' ') for x in data.splitlines()]]

    SCORES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
              'T': 10, 'J': 0, 'Q': 12, 'K': 13, 'A': 14}

    cmp = []
    for h in hands:
        c = dict(Counter(h[0]))

        # handle jokers
        cj = c.get('J', 0)
        c['J'] = 0
        if cj == 5:
            c['A'] = 5
        else:
            mc = max(c.items(), key=lambda x: x[1])
            c[mc[0]] += cj

        # format abcde
        value_sort = sorted(c.values(), reverse=True)
        M0 = [10**x for x in range(5)][::-1]
        m0 = sum([ a*b for a,b in zip(value_sort, M0) ])

        # format ffgghhiijj
        M1 = [100**x for x in range(5)][::-1]
        m1 = sum([ SCORES[a]*b for a,b in zip(h[0], M1) ])

        cmp.append((m0 * 100**5 + m1, h[0], h[1]))

    s = sorted(cmp)
    return reduce(lambda a,b: a + b[0]*b[1][2], enumerate(s, start=1), 0)

# 250757288
