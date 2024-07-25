from sys import stdin as s
import heapq

#s = open("20136/input.txt", "rt")
tot = 0
holeCount, n = map(int, s.readline().split())
arr = list(map(int, s.readline().split()))
hole = []
inf = float('inf')
next = [[inf] for _ in range(n+1)]
for i in range(len(arr)-1, -1, -1):
    next[arr[i]].append(i)
heapq.heapify(hole)
holePlugged = [False for _ in range(n+1)]
holePluggedCount = 0
for i in range(len(arr)):
    if holePluggedCount<holeCount and holePlugged[arr[i]]==False: # 플러그가 다 안 꽂혔을 때
        holePlugged[arr[i]] = True
        holePluggedCount += 1
        next[arr[i]].pop()
        heapq.heappush(hole, (next[arr[i]][-1]*-1, arr[i]))
    elif holePlugged[arr[i]]: # 이미 꽂혀있는 경우
        next[arr[i]].pop()
        heapq.heappush(hole,(next[arr[i]][-1]*-1, arr[i]))

        
        # 사실 여기서 힙큐를 업데이트 쳐줘야하는데 어케 기존거를 찾아서 pop 하지?ㅠㅠ
        # for j in range(len(hole)):
        #     x,y = hole[j]
        #     if y == arr[i]:
        #         hole[j]=(next[arr[i]][-1]*-1, arr[i])
        #         heapq.heapify(hole)
        #         break
        #완전탐색했따그냥
    else: # 꽂혀있던 걸 빼야하는 경우
        a, b = heapq.heappop(hole)
        tot += 1
        holePlugged[b] = False
        holePlugged[arr[i]] = True
        next[arr[i]].pop()
        heapq.heappush(hole, (next[arr[i]][-1]*-1, arr[i]))

print(tot)
