example = '''\
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
'''

def part1(data):
    #data = example
    fields = data.split('\n\n')

    s = 0
    for field in fields:
        lines = field.splitlines()

        foo = 0
        for m in range(1, len(lines)):
            t = map(lambda x: x[0]==x[1], zip(lines[:m][::-1], lines[m:]))
            if all(t):
                foo += 100*m

        for m in range(1, len(lines[0])):
            transposed = list(zip(*lines))

            t = map(lambda x: x[0]==x[1], zip(transposed[:m][::-1], transposed[m:]))
            if all(t):
                foo += m

        assert(foo > 0)
        s += foo

    return s


def part2(data):
    # data = example
    fields = data.split('\n\n')

    s = 0
    for field in fields:
        lines = field.splitlines()

        foo = 0
        for m in range(1, len(lines)):
            g = zip(lines[:m][::-1], lines[m:])
            t = sum( a != b for c,d in g for a,b in zip(c, d) )

            if t == 1:
                foo += 100*m

        for m in range(1, len(lines[0])):
            transposed = list(zip(*lines))
            g = zip(transposed[:m][::-1], transposed[m:])
            t = sum( a != b for c,d in g for a,b in zip(c, d) )

            if t == 1:
                foo += m

        assert(foo > 0)
        s += foo

    return s
