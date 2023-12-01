import string

def part1(data):
    s = 0
    for line in data.splitlines():
        d = list(filter(lambda x: x in string.digits, line))
        s += int(d[0] + d[-1])
    return s

def part2(data):
    lut = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    for k,v in lut.items():
        data = data.replace(k, f'{k}{v}{k}')
    return part1(data)
