example = '''7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
'''

import itertools
import math

PIPES = {
    '|': (0, 2),
    '-': (1, 3),
    'L': (0, 1),
    'J': (0, 3),
    '7': (2, 3),
    'F': (1, 2),
}

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def walk(lines, initial_start, initial_dir):
    pos = initial_start
    dir = initial_dir
    while True:
        pos = (pos[0]+DIRS[dir][0], pos[1]+DIRS[dir][1])
        char = lines[pos[0]][pos[1]]

        yield (pos, char)

        dirs = PIPES[char]
        dir = dirs[0] if dirs[0] != (dir+2)%4 else dirs[1]

def part1(data):
    #data = example

    lines = data.splitlines()

    start = (0,0)
    for y,line in enumerate(lines):
        if (x := line.find('S')) >= 0:
            start = (y, x)
            break

    count = 0
    for _,c in walk(lines, start, 1):
        if c == 'S':
            break
        count += 1

    return math.ceil(count/2)

def part2(data):
    example = '''FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
'''
#    example = '''...........
#.S-------7.
#.|F-----7|.
#.||.....||.
#.||.....||.
#.|L-7.F-J|.
#.|..|.|..|.
#.L--J.L--J.
#...........
#'''

    #data = example

    lines = data.splitlines()
    edge = (len(lines), len(lines[0]))

    start = (0,0)
    for y,line in enumerate(lines):
        if (x := line.find('S')) >= 0:
            start = (y, x)
            break

    walls_v = set()
    walls_rest = set()
    #for p,c in walk(lines, start, 2):  # example dir
    for p,c in walk(lines, start, 1):  # real
        if c == '|':
            walls_v.add(p)
        else:
            walls_rest.add(p)
        if c == 'S':
            break

    lines[start[0]] = lines[start[0]].replace('S', 'F')

    walls_all = walls_v | walls_rest

    in_bounds = set()
    out_bounds = set()
    #for y,line in enumerate(lines[1:2], start=1):
    #for y,line in enumerate(lines[5:6], start=5):
    for y,line in enumerate(lines):
        for x,c in enumerate(line):
            if (y,x) in walls_all:
                continue

            #print('new char')
            enc_count = 0
            state = None
            for i in range(edge[1]-x):
                char = line[x+i]
                #print(state, i, (y, x+i), (y, x+i) in walls_rest, char)

                if not state:
                    #print('ns')
                    if char in ('L', 'F') and (y, x+i) in walls_all:
                        state = char
                    elif (y, x+i) in walls_v:
                        #print('inc?')
                        enc_count += 1
                else:
                    if (y, x+i) in walls_all:
                        if state == 'L' and char == '7':
                            state = None
                            enc_count += 1
                            #print('inc? L')
                        elif state == 'F' and char == 'J':
                            state = None
                            enc_count += 1
                            #print('inc? F')
                        elif state == 'L' and char == 'J':
                            state = None
                        elif state == 'F' and char == '7':
                            state = None


            if enc_count % 2 == 1:
                in_bounds.add((y,x))
            else:
                out_bounds.add((y,x))

    # print(len(out_bounds))
    # print(out_bounds)
    # print(len(in_bounds))
    # print(sorted(in_bounds))

    return len(in_bounds)
