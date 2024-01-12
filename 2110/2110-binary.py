a, b = map(int,input().split())
arr = []
for i in range(a):
    arr.append(int(input()))
arr.sort()

start = 1
end = arr[-1] - arr[0]
result = 0

while start <= end:
    mid = (start + end) // 2 #지금부터 조질 값
    value = arr[0] #앞에서부터
    count = 1
    for i in range(1, len(arr)):
        if arr[i] >= value + mid:
            value = arr[i]
            count += 1
    if count >= b: #만약에 되는거면 , mid를 늘려야됨
        start = mid + 1
        result = mid
    else: #만약에 안되는거면, mid를 줄여야됨
        end = mid - 1

start = 1
end = arr[-1] - arr[0]
result2 = 0
while start <= end:
    mid = (start + end) // 2 #지금부터 조질 값
    value = arr[-1] #뒤에서부터
    count = 1
    for i in range(len(arr)-2, -1, -1):
        if arr[i] <= value - mid:
            value = arr[i]
            count += 1
    if count >= b: #만약에 되는거면,mid를 늘여야됨
        start = mid + 1
        result2 = mid
    else:#만약에 안되는거면, mid를 줄여야됨
        end = mid - 1

#print(result, result2)
print(max(result,result2))