import heapq

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
heapq.heapify(arr)
total = 0
for i in range(n-1):
    min1 = heapq.heappop(arr)
    min2 = heapq.heappop(arr)
    total = total+min1+min2
    heapq.heappush(arr,min1+min2)
print(total)