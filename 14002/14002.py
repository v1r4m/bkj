n = int(input())
arr = list(map(int, input().split()))
#n = 16
#arr = [10,30,50,90,50,10,11,12,13,14,15,16,17,18,19,20]

dp = [1] * n  
index = [-1] * n #기록용
maximum = 1

for i in range(n): # … ,j , i , ….
    for j in range(i):
        if arr[i] > arr[j]: #늘어나는 방향이고(같으면안됨)
            if dp[i] <= dp[j] : #지금까지 본 것보다 같거나 더 좋은 결과가 나오면
                dp[i] = dp[j] + 1
                index[i] = j #나중에 최종값으로 바뀜, 기록용

###끝ㅌㅌㅌㅌㅌ
result = []
maximum = max(dp) # O(n). 마지막 점
maxResult = dp.index(maximum)
a = maxResult
for i in range(maximum):
    result.append(arr[a])
    a = index[a]
result.reverse()

print(maximum)
print(*result)