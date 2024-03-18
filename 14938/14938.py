from sys import stdin as s

#s = open("14938/input.txt", "rt")

location,searchArea,roadCount = map(int,s.readline().split())
item = list(map(int,s.readline().split()))
arr = [[float('inf') for i in range(location+1)] for j in range(location+1)]
for i in range(roadCount):
    a,b,c = map(int,s.readline().split())
    arr[a][b] = c
    arr[b][a] = c

for i in range(location+1):
    arr[i][i] = 0
for k in range(1,location+1): # 기준점
    for i in range(1,location+1):
        for j in range(1,location+1):
            arr[i][j] = min(arr[i][j],arr[i][k]+arr[k][j])
#print(arr)
result = [0 for i in range(location+1)]
for i in range(1,location+1):
    for j in range(1,location+1):
        if arr[i][j] <= searchArea:
            result[i] += item[j-1] #인덱스
print(max(result))
            
