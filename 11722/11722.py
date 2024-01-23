n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
dp1 = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]: #감소하는 방향이고
            if dp1[i] <= dp1[j]:
                dp1[i] = dp1[j] + 1

print(max(dp1))