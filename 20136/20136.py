from sys import stdin as s
import heapq

s = open("20136/input.txt", "rt")
tot = 0
holeCount, n = map(int, s.readline().split())
arr = list(map(int, s.readline().split()))
hole = []
next = [0 for _ in range(n+1)]
for i in range(n):
    next[arr[i]] += 1
for i in range(holeCount):
    hole.append((next[arr[i]]-1, arr[i]))
heapq.heapify(hole)
holePlugged = [False for _ in range(n+1)]
for i in range(holeCount):
    holePlugged[arr[i]]= True
    next[arr[i]] -= 1
for i in range(holeCount,n):
    if holePlugged[arr[i]]:
        next[arr[i]] -= 1
    else:
        a, b = heapq.heappop(hole)
        tot += 1
        holePlugged[b] = False
        holePlugged[arr[i]] = True
        heapq.heappush(hole, (next[arr[i]]-1, arr[i]))
        next[arr[i]]-= 1



print(hole, n, arr)

