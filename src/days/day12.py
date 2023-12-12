example = '''???.###. 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
'''

def is_valid(state, groups):
    cnt = 0
    g = list(groups)[::-1]

    for c in state:
        if c == '#':
            cnt += 1
        elif c == '.':
            if cnt > 0:
                try:
                    if cnt != g.pop():
                        return False
                except IndexError:
                    return False
                cnt = 0
        else:
            print('err?')

    if cnt > 0:
        try:
            if cnt != g.pop():
                return False
        except IndexError:
            return False
    return len(g) == 0

def solve(state, groups, res=0):
    try:
        f = state.index('?')
    except ValueError:
        return res + is_valid(state, groups)

    for o in ('#', '.'):
        state[f] = o
        res += solve(state, groups)
    state[f] = '?'

    return res

def part1(data):
    #data = example

    parsed = [ (x[0], tuple(map(int, x[1].split(','))))
              for x in [ line.split() for line in data.splitlines() ] ]

    s = 0
    for state, groups in parsed:
        s += solve(list(state), groups)
    return s
