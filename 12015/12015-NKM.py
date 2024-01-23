n = int(input())
arr = list(map(int, input().split()))
binary = []

def binaryCal(num, binary):
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

for i in range(n):
    binaryCal(arr[i],binary)

print(len(binary))