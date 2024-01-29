n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
# 10 20 30
# a b c
# a + b + a + b + c
# 2a + 2b + c
#3의 경우에서는 그렇다. 그러면 4의 경우에서는?
# 10 20 30 40
# a b c d
# a + b + a + b + c + a + b + c + d
# a + b + c + d + a + b + c + d
# 2a + 2b + 2c + 2d
# 3a + 3b + 2c + d
# (n-1)a + (n-1)b + (n-2)c + d
# 그러면 d부터 최대가 되어야 한다. 
if n == 1:
    print(arr[0])
else:
    arr.sort()
    arr.reverse()
    print(arr)
    total = 0
    for i in range(0,n-2):
        total = total + arr[i] * (i+1)
    total = total + arr[n-2]*(n-1)
    total = total + arr[n-1]*(n-1)
    print(total)
#틀렸습니다가 왜 나오지?
#만약 한 개 있으면?