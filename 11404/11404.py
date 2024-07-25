from sys import stdin as s

s = open("11404/input.txt", "rt")

n = int(s.readline())
point = [[float('inf') for i in range(n)] for j in range(n)]
count = int(s.readline())
for i in range(count):
    a, b, distance = map(int, s.readline().split())
    if point[a-1][b-1]>distance:
        point[a-1][b-1] = distance
for i in range(n):
    point[i][i] = 0
#i->j->k
for cc in range(n):
    for i in range(n):
        for k in range(n):
            for j in range(n):
                if point[i][j]+point[j][k] < point[i][k]:
                    point[i][k] = point[i][j]+point[j][k]
for i in range(n):
    for j in range(n):
        if point[i][j]==float('inf'):
            print(0, end=' ')
        else:
            print(point[i][j], end=' ')
    print()




# 3 -> 1(mid) -> 5 -> 7

# 1(mid)->7 ? 






3 -> 1 (mid) -> 2 -> 5

3-> 5: inf

3->2 : 4


