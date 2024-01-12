a, b = map(int,input().split())
arr = []
for i in range(a):
    arr.append(int(input()))
arr.sort()

diff = [arr[i+1] - arr[i] for i in range(a-1)]
diff.sort()

ans = diff[0]
count = 1
for i in range(1, len(diff)):
    if diff[i] >= ans:
        count += 1
        if count == b:
            break
    else:
        ans = diff[i]

print(ans)