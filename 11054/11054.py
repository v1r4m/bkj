
import copy

n = int(input())
arr = list(map(int, input().split()))
# n = 10
# arr = [1,5,2,1,4,3,4,5,2,1]

dp1 = [1] * n 
dp2 = [1] * n 
maximum1 = 1
maximum2 = 1

for i in range(n): # … ,j , i , ….
    for j in range(i):
        if arr[i] > arr[j]: #늘어나는 방향이고(같으면안됨)
            if dp1[i] <= dp1[j] : #지금까지 본 것보다 같거나 더 좋은 결과가 나오면
                dp1[i] = dp1[j] + 1

arr2 = copy.deepcopy(arr[::-1])
for i in range(n): # … ,j , i , ….
    for j in range(i):
        if arr2[i] > arr2[j]: #늘어나는 방향이고(같으면안됨)
            if dp2[i] <= dp2[j] : #지금까지 본 것보다 같거나 더 좋은 결과가 나오면
                dp2[i] = dp2[j] + 1
dp3 = copy.deepcopy(dp2[::-1])


print(max([x+y for x,y in zip(dp1, dp3)])-1)