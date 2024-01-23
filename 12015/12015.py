import heapq

# a = int(input())
# arr = list(map(int, input().split()))
a = 6
arr = [10,20,10,30,20,50]
dp1 = [1]*a
dp2 = [[1,1]]*a
heapq.heapify(dp2)
for i in range(a-1):
    if arr[i] < arr[i+1]: #늘어나는 방향이면
        if dp1[i+1] <= dp1[i]:
            dp1[i+1] = dp1[i] + 1
            heapq.heappush(dp2,[dp1[i+1],arr[i+1]])
    else: #늘어나지 않는다면
        dp2.append([dp1[i],arr[i]])
        for j in range(len(dp2)):
            key, ar = dp2[j]
            if ar < arr[i+1]:
                dp1[i+1] = key + 1
                heapq.heappush(dp2,[dp1[i+1],arr[i+1]])
                break

print(max(dp1))