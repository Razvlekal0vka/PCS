a, b = list(map(int, input().split()))
n, m = list(map(int, input().split()))
t1, t2 = 0, b * m
while t1 + t2 != n:
    t1, t2 = t1 + a, t2 - b
print(t1, t2)

# без 10, 12, 13
