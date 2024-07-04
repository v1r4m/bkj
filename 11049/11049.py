from sys import stdin as s

s = open("11049/input.txt", "rt")

n = int(s.readline())
arr = [list(map(int, s.readline().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
#first row
for i in range(n-1):
    dp[i][i+1] = arr[i][0]*arr[i][1]*arr[i+1][1]

for i in range(2, n):
    for j in range(n-i):
        candidate = []
        #dp[j][j+i]
        for k in range(i):
            # print(dp[j][j+i-k-1])
            # print(dp[j+i-k-1][j+i])
            # print(arr[j][0])
            # print(arr[j+i-k-1][1])
            # print(arr[j+i][1])
            candidate.append(dp[j][j+i-k-1] + dp[j+i-k][j+i] + arr[j][0]*arr[j+i-k-1][1]*arr[j+i][1])
        dp[j][j+i] = min(candidate)
#         print(candidate)
# print(dp)

print(dp[0][n-1])