n,m = map(int,input().split())
from itertools import combinations
arr = []
for i in range(n):
    arr.append(i+1)
result = list(combinations(arr,m))

for i in range(len(result)):
    for j in range(m):
        print(result[i][j],end=" ")
    print()