from collections import deque

n,m = map(int,input().split())
arr = [[] for i in range(n+1)]
for i in range(n-1):
    a,b,distance = map(int,input().split())
    arr[a].append([b,distance])
    arr[b].append([a,distance])

def get_distance(start,end,arr):
    deq = deque()
    for i in range(len(arr[start])):
        deq.append([start,arr[start][i][0],arr[start][i][1]])
    while deq:
        a,b,distance = deq.popleft()
        if b == end:
            return distance
        else:
            for i in range(len(arr[b])):
                if arr[b][i][0] != a:
                    deq.append([b,arr[b][i][0],distance+arr[b][i][1]])

for i in range(m):
    a,b = map(int,input().split())
    print(get_distance(a,b,arr))