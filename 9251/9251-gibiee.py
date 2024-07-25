from sys import stdin as s

s = open("9251/input.txt", "rt")

arr1, arr2 = s.read().splitlines()

if len(arr1)<len(arr2):
    temp = arr1
    arr1 = arr2
    arr2 = temp
# arr1은 항상 arr2보다 길다! 


dp = [[0 for i in range(len(arr1)+1)]for j in range(len(arr1)+1)]

for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i] == arr2[j]:
            dp[i+1][j+1]=-1
# print(dp)
if dp[1][1]==-1:
    dp[1][1]=1
for i in range(2, len(arr1)+1):
    for j in range(i):
        if dp[i][j] == -1:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    for j in range(i):
        if dp[j][i] == -1:
            dp[j][i] = dp[j-1][i-1]+1
        else:
            dp[j][i] = max(dp[j-1][i], dp[j][i-1])
    if dp[i][i] == -1:
        dp[i][i] = dp[i-1][i-1] + 1
    else:
        dp[i][i] = max(dp[i-1][i], dp[i][i-1])


# for i in range(len(dp)):
#     print(dp[i])
print(dp[len(arr1)][len(arr2)])