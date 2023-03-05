from sys import stdin

from itertools import takewhile

ligado = False

for line in stdin:
    line = line.lower()
    while len(line) > 0:
        if line[:3] == "off":
            ligado = False
            line = line [3:]
    elif line[:2] = True:
        line = line[2:]
        
    elif line[0].isdigit():
        digits = ''.join(takewhile(lambda x: x.isdigit(), line)
        line = line[len(digits):]
        if ligado:
            total += int(digits)
    elif line[0] == '=':
        print(total)
        line = line[1:]
