a, b = list(map(int, input().split()))
d = b - a
n, m = list(map(int, input().split()))
c2 = (n // b) * b
c1 = a * (m - (n // b))
while c1 + c2 != n:
    if (n - c1 - c2) % d:
        c1 = c1 + a * (n - c1 - c2) // d
        c2 = c2 - b * (n - c1 - c2) // d
        break
    else:
        c2 -= b
        c1 += a
print(c1, c2)
