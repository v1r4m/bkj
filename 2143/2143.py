s = open("input.txt", "rt")

t = int(s.readline().strip())
n = int(s.readline().strip())
arr1 = list(map(int, s.readline().split()))
m = int(s.readline().strip())
arr2 = list(map(int, s.readline().split()))
arr1sumCount = {}
arr2sumCount = {}
for i in range(n):
    for j in range(1,n-i+1):
        sumTemp = sum(arr1[i:i+j])
        if sumTemp in arr1sumCount:
            arr1sumCount[sumTemp] += 1
        else:
            arr1sumCount[sumTemp] = 1
for i in range(m):
    for j in range(1,m-i+1):
        sumTemp = sum(arr2[i:i+j])
        if sumTemp in arr2sumCount:
            arr2sumCount[sumTemp] += 1
        else:
            arr2sumCount[sumTemp] = 1
answer = 0
# print(arr1sumCount, arr2sumCount)
for sumKey1 in arr1sumCount:
    sumKey2 = t - sumKey1
    if sumKey2 in arr2sumCount:
        answer = answer + arr1sumCount[sumKey1]*arr2sumCount[sumKey2]
print(answer)
