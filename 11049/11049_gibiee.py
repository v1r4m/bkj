from sys import stdin as s
# s = open("input.txt", "rt")

N = int(s.readline().strip())

nums = []
for i in range(N) :
    r, c = map(int, s.readline().split())
    nums.append([r,c])

dp = [[None] * (N) for _ in range(N)]
for i in range(N) :
    for j in range(N-i) :
        y, x = j, i+j

        if y == x :
            r, c = nums[y]
            dp[y][x] = 0
        else :
            # dp를 채울 때 양옆 2가지가 아니라, 가능한 모든 경우의 수를 반복해야함!
            for k in range(y, x) :
                r1, c1 = nums[y]
                r2, c2 = nums[k]
                r3, c3 = nums[x]
                
                w = r1 * c2 * c3
                if dp[y][x] == None : dp[y][x] = dp[y][k] + dp[k+1][x] + w
                else : dp[y][x] = min(dp[y][x], dp[y][k] + dp[k+1][x] + w)

print(dp[0][-1])