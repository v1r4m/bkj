a, b = map(int,input().split())
def str_to_list(string):
    return [int(i) for i in string]
arr = []
for i in range(a):
    arr.append(str_to_list(input()))

# a, b = 4, 4
# arr = [[0,0,1,0],
#        [1,1,1,0],
#        [0,1,1,1],
#        [0,1,0,0]]
# a,b=5,5
# arr = [[0,0,0,1,0],[1,1,1,1,0],[0,1,1,1,0],[0,1,1,1,1],[0,1,1,1,0]]
dp = [[None for i in range(b)] for j in range(a)]

for i in range(a):
    dp[i][0] = arr[i][0]
for i in range(b):
    dp[0][i] = arr[0][i]
#위-왼쪽 한줄은 그냥 채워준다

for i in range(1,a):
    for j in range(1,b):
        if arr[i][j] == 0:
            dp[i][j] = 0
        else: #1
            if arr[i-1][j-1] and arr[i-1][j] and arr[i][j-1]:
                if dp[i-1][j-1] == dp[i-1][j] == dp[i][j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
            else:
                dp[i][j] = 1

maximus = 0
for i in range(a):
    for j in range(b):
        if dp[i][j] > maximus:
            maximus = dp[i][j]

print(maximus*maximus)


        
