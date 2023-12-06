example = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
'''
import re
import functools


def parse(data):
    map_strs = data.split(':')
    pat = re.compile(r'(\d+) (\d+) (\d+)')

    maps = []
    for m in map_strs[1:]:
        d = pat.findall(m)
        t = [(int(x), int(y), int(z)) for x,y,z in d]
        maps.append(t)
    return maps


def conv(s, mapset: tuple):
    for m in mapset:
        delta = s - m[1]
        if 0 <= delta < m[2]:
            return m[0] + delta
    return s


def part1(data):
    #data = example

    data = data.split('\n', 1)
    seeds = list(map(int, data[0].split(' ')[1:]))
    maps = parse(data[1])

    for mapset in maps:
        seeds = [conv(s, mapset) for s in seeds]
    return min(seeds)


def part2(data):
    #data = example

    data = data.split('\n', 1)
    maps = parse(data[1])

    s = list(map(int, data[0].split(' ')[1:]))
    seedranges = [ tuple(s[x:x+2]) for x in range(0, len(s), 2) ]
    
    for mapset in maps:
        mapped = []

        while len(seedranges) > 0:
            s = seedranges.pop(0)

            for m in mapset:
                ol = (max(s[0], m[1]), min(s[0]+s[1], m[1]+m[2]))

                if ol[0] < ol[1]:
                    # There is overlap between the ranges

                    # map overlap
                    m_ = (ol[0] + (m[0]-m[1]), ol[1]-ol[0])
                    mapped.append(m_)

                    # add gt and lt parts back to seedranges if len is > 0
                    lt = (s[0], ol[0]-s[0])
                    gt = (ol[1], s[0]+s[1]-ol[1])
                    seedranges += [ x for x in [lt, gt] if x[1] > 0 ]

                    # Break from current mapset handling, as the non-mapped
                    # parts of the seed are in a new seedrange
                    break
                else:
                    # There is no overlap between seedrange and all maps in set
                    continue
            else:
                # Did not break, so no overlap. Map whole range to itself
                mapped.append(s)

        # Done handling mapset, pepare for next
        seedranges = mapped

    return sorted(seedranges)[0][0]
