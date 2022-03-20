

n, m = list(map(int, input().split()))
com = input()
x, y = 0, 0
k = 0
while k < m:
    for e in com:
        if k < m:
            k += 1
            if e == 'N':
                y += 1
            elif e == 'E':
                x += 1
            elif e == 'S':
                y -= 1
            elif e == 'W':
                x -= 1
        else:
            break
print(x, y)