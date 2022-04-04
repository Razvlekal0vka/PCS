s = ['a', 'b', 'c', 'd', 'e']
b = set()
for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                i = i1 + i2 + i3 + i4
                n1 = n2 = n3 = n4 = 0
                for j in s:
                    n1 += 1
                    if j == i1:
                        break

                for j in s:
                    n2 += 1
                    if j == i2:
                        break

                for j in s:
                    n2 += 1
                    if j == i2:
                        break

                for j in s:
                    n2 += 1
                    if j == i2:
                        break

                h = 0

                if abs(n1 - n2) > 1:
                    h += 1

                if abs(n2 - n3) > 1:
                    h += 1

                if abs(n3 - n4) > 1:
                    h += 1

                if h <= 1:
                    b.add(i)
                print(len(b))