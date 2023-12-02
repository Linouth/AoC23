'''
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
'''
import re

def part1(data):
    MAX = (12, 13, 14)

    s = 0
    for i,line in enumerate(data.splitlines()):
        print(line)

        games = (line.split(': ')[1]).split('; ')
        for g in games:
            res = re.findall('(\d+)(?= red)|(\d+)(?= green)|(\d+)(?= blue)', g)
            col = ('', '', '')
            for r in res:
                col = ( col[0] or r[0], col[1] or r[1], col[2] or r[2] )
            col = (int(col[0] or 0), int(col[1] or 0), int(col[2] or 0))

            if col[0] > MAX[0] or col[1] > MAX[1] or col[2] > MAX[2]:
                break
        else:
            s += i+1

    return s


def part2(data):
    s = 0
    for i,line in enumerate(data.splitlines()):
        print(line)
        req = (0, 0, 0)

        games = (line.split(': ')[1]).split('; ')
        for g in games:
            res = re.findall('(\d+)(?= red)|(\d+)(?= green)|(\d+)(?= blue)', g)
            col = ('', '', '')
            for r in res:
                col = ( col[0] or r[0], col[1] or r[1], col[2] or r[2] )
            col = (int(col[0] or 0), int(col[1] or 0), int(col[2] or 0))

            req = (max(req[0], col[0]),
                   max(req[1], col[1]),
                   max(req[2], col[2]))
        print(req)
        s += req[0] * req[1] * req[2]

    return s
