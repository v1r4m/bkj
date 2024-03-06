t = int(input())
arr = []
for i in range(1,62):
    arr.append((i**2-(i-1)**2)/2+(i-1)**2)
    arr.append(i**2)
for i in range(t):
    now, goal = map(int, input().split())
    diff = goal - now
    sqrt_diff = diff ** 0.5
    for i in range(len(arr)):
        if(arr[i] >= sqrt_diff):
            if(int(arr[i])==arr[i]):
                print(arr[i])
            else:
                print(int(arr[i])+1)
            break
