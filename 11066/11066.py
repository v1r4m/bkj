from sys import stdin as s

# s = open("11066/input.txt", "rt")
tot = int(s.readline())
for totIndex in range(tot):
    n = int(s.readline())
    arr = list(map(int, s.readline().split()))

    dp = [[(0,0)]*n for _ in range(n)]
    #first row
    for i in range(n):
        dp[i][i] = (arr[i],0)

    for i in range(1, n):
        for j in range(n-i):
            candidate = []
            #dp[j][j+i]
            for k in range(i):
                candidate.append((dp[j][j+i-k-1][0] + dp[j+i-k][j+i][0], dp[j][j+i-k-1][0] + dp[j+i-k][j+i][0] + dp[j][j+i-k-1][1] + dp[j+i-k][j+i][1]))
            
            dp[j][j+i] = min(candidate, key=lambda x: x[1])
    # #         print(candidate)
    # print(dp)

    print(dp[0][n-1][1])