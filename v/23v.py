import sys

lines = []
for l in sys.stdin:
    l = l.replace('\n', '')
    lines.append(l)

n, m = list(map(int, lines[0].split()))
com1 = lines[1]
x, y = 0, 0
k = 0
while k < m:
    if k == 0:
        com = com1
    if len(com) == 0:
        com = com1
    if k < m:
        k += 1
        if 'N' in com:
            print('N', com)
            com = com.replace('N', '', 1)
            y += 1
        elif 'E' in com:
            print('E', com)
            com = com.replace('E', '', 1)
            x += 1
        elif 'S' in com:
            print('S', com)
            com = com.replace('S', '', 1)
            y -= 1
        elif 'W' in com:
            print('W', com)
            com = com.replace('W', '', 1)
            x -= 1
print(x, y)

# не работ ошибка в порядке