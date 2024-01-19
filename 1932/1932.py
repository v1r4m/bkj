a = int(input())
arr = []
for i in range(a):
    temp = list(map(int,input().split()))
    arr.append(temp)
dp = [[0 for i in range(a)] for i in range(a)]
dp[0][0] = arr[0][0]
for i in range(1,len(arr)):
    dp[i][0] = dp[i-1][0]+arr[i][0]
    for j in range(1,len(arr[i])):
        dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + arr[i][j]
print(max(dp[a-1]))
