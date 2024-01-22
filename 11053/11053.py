a = int(input())
arr = list(map(int, input().split()))
dp1 = [1] * a
for i in range(a):
    for j in range(i):
        if arr[i] > arr[j]:
            if dp1[i] <= dp1[j]:
                dp1[i] = dp1[j] + 1
print(max(dp1))