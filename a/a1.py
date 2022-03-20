a, b = list(map(int, input().split()))
n, m = list(map(int, input().split()))
c1 = 0
c2 = b * m
while c1 + c2 != n:
    c2 -= b
    c1 += a
print(c1, c2)