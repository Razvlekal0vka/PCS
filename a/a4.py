import numpy

x1, y1, z1 = list(map(int, input().split()))
vx1, vy1, vz1 = list(map(int, input().split()))
x2, y2, z2 = list(map(int, input().split()))
vx2, vy2, vz2 = list(map(int, input().split()))

r1 = [x1, y1, z1]
s1 = [vx1, vy1, vz1]

r2 = [x2, y2, z2]
s2 = [vx2, vy2, vz2]

R = [x2 - x1, y2 - y1, z2 - z1]

matrix1 = [R, s1, s2]
Matrix = numpy.matrix(matrix1)
D = numpy.linalg.det(Matrix)
print(D)

r =
print(r)

min_d = abs(D) / abs(r)
print(min_d)
