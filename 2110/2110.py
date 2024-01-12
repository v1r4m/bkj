a, b = map(int,input().split())
arr = []
for i in range(a):
    arr.append(int(input()))
arr.sort()
# a, b = 7, 4
# arr = [1,3,5,13,17,23,40]
diff = []
for i in range(a-1):
    diff.append(arr[i+1]-arr[i])
diff.append(diff[-1])
difference = arr[-1]-arr[0]
guide = difference // (b-1)

ans = []
pivot = 0
i = 0
while i<(a):
    pivot += diff[i]
    if pivot>=guide:
        ans.append(pivot)
        pivot = diff[i]
    i += 1

print(min(ans))
