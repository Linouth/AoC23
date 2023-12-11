example2 = '''...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
'''

from itertools import combinations


def part1(data, inc=1):
    lines = data.splitlines()

    empty_rows = set(range(len(lines)))
    empty_cols = set(range(len(lines[0])))

    galaxies = []
    for y,line in enumerate(lines):
        for x,c in enumerate(line):
            if c != '.':
                galaxies.append( (y,x) )
                empty_rows.discard(y)
                empty_cols.discard(x)

    s = 0
    for g0, g1 in combinations(galaxies, 2):
        y_dst, x_dst = abs(g0[0]-g1[0]), abs(g0[1]-g1[1])

        y0, y1 = min(g0[0], g1[0]), max(g0[0], g1[0])
        for r in empty_rows:
            if y0 < r < y1:
                y_dst += inc

        x0, x1 = min(g0[1], g1[1]), max(g0[1], g1[1])
        for c in empty_cols:
            if x0 < c < x1:
                x_dst += inc

        dst = y_dst + x_dst

        s += dst
    return s


def part2(data):
    return part1(data, inc=1000000-1)
