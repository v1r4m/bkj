import heapq

n = int(input())
arr = list(map(int, input().split()))
binary = []
binaryDp = [0]*n

def binaryCal(num, binary,idx):
    start = 0
    end = len(binary)-1
    while start <= end:
        mid = (start+end)//2
        if binary[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    if start > len(binary)-1:
        binary.append(num)
    else:
        binary[start] = num
    binaryDp[idx] = start

for i in range(n):
    binaryCal(arr[i],binary,i)

print(len(binary))
temp = []
maximum = max(binaryDp)
for i in range(n-1,-1,-1):
    if binaryDp[i]==maximum:
        maximum=binaryDp[i]-1
        temp.append(arr[i])
temp.reverse()
for i in range(len(temp)):
    print(temp[i], end = " ")


