from sys import stdin as s

s = open("11660/input.txt", "rt")

a,b = map(int, s.readline().split())
arr = []
for i in range(a):
    arr.append(list(map(int, s.readline().split())))
dp = [[0 for i in range(a)] for j in range(a)]
for i in range(a):
    for j in range(a):
        if i == 0 and j == 0:
            dp[i][j] = arr[i][j]
        elif i == 0:
            dp[i][j] = dp[i][j-1]+arr[i][j]
        elif j == 0:
            dp[i][j] = dp[i-1][j]+arr[i][j]
        else:
            dp[i][j] = dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+arr[i][j]
for i in range(b):
    x1, y1, x2, y2 = map(int, s.readline().split())
    # result = 0
    # for j in range(x1-1, x2):
    #     for k in range(y1-1, y2):
    #         result += arr[j][k]
    # print(result)
    if x1 == 1 and y1 == 1:
        print(dp[x2-1][y2-1])
    elif x1 == 1:
        print(dp[x2-1][y2-1]-dp[x2-1][y1-2])
    elif y1 == 1:
        print(dp[x2-1][y2-1]-dp[x1-2][y2-1])
    else:
        print(dp[x2-1][y2-1]-dp[x2-1][y1-2]-dp[x1-2][y2-1]+dp[x1-2][y1-2])

