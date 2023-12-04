example = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
'''
import re
import functools


@functools.cache
def parse_cards(data):
    col = data.find(':')
    bar = data.find('|')

    parsed = []
    for line in data.splitlines():
        winning = re.findall(r'\d+', line[col+1:bar])
        got = re.findall(r'\d+', line[bar+1:])
        won = list(filter(lambda x: x in winning, got))
        parsed.append(len(won))
    return parsed


def part1(data):
    return sum([2**(x-1) if x>0 else 0 for x in parse_cards(data)])


def part2(data):
    parsed = parse_cards(data)

    s = 0
    cards = [1] * len(parsed)
    for i,ccount in enumerate(cards):
        s += ccount
        p = parsed[i]
        for k in range(i+1, i+p+1):
            cards[k] += ccount
    return s
