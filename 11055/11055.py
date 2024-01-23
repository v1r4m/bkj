n = int(input())
arr = list(map(int, input().split()))
dp1 = arr.copy()

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]: # 증가하는 방향이면
            if dp1[i] < dp1[j]+arr[i]:
                dp1[i] = dp1[j] + arr[i]

print(max(dp1))