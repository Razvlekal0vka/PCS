'''x, y = 0, 0
n, m = list(map(int, input().split()))
com = input()
s = 0
while m > 0:
    s = s % len(com)
    if com[s] == 'N':
        y += 1
        m -= 1
    if com[s] == 'E':
        x += 1
        m -= 1
    if com[s] == 'S':
        y -= 1
        m -= 1
    if com[s] == 'W':
        x -= 1
        m -= 1
    s += 1
print(x, y)
'''


n, m = list(map(int, input().split()))
com = input()[:n]
res_com = com * (m // len(com)) + com[:(m % len(com))]
y, x = res_com.count('N') - res_com.count('S'), res_com.count('E') - res_com.count('W')
print(x, y)
