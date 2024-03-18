from sys import stdin as s

import copy

# s = open("2096/2096.txt", "rt")

a = int(s.readline())
arr = []
dpSmall = [[0,0,0],[0,0,0]]
dpBig = [[0,0,0],[0,0,0]]
for i in range(a):
    temp = list(map(int,s.readline().split()))
    arr.append(temp)
if a == 1:
    maxi = max(arr[0])
    mini = min(arr[0])
else:
    dpSmall[0]=copy.deepcopy(arr[0])
    dpBig[0]=copy.deepcopy(arr[0])
    for i in range(1,a):
        dpSmall[1][0]=min(dpSmall[0][0]+arr[i][0],dpSmall[0][1]+arr[i][0])
        dpSmall[1][1]=min(dpSmall[0][0]+arr[i][1],dpSmall[0][1]+arr[i][1],dpSmall[0][2]+arr[i][1])
        dpSmall[1][2]=min(dpSmall[0][1]+arr[i][2],dpSmall[0][2]+arr[i][2])
        dpSmall[0]=copy.deepcopy(dpSmall[1])
    for i in range(1,a):
        dpBig[1][0]=max(dpBig[0][0]+arr[i][0],dpBig[0][1]+arr[i][0])
        dpBig[1][1]=max(dpBig[0][0]+arr[i][1],dpBig[0][1]+arr[i][1],dpBig[0][2]+arr[i][1])
        dpBig[1][2]=max(dpBig[0][1]+arr[i][2],dpBig[0][2]+arr[i][2])
        dpBig[0]=copy.deepcopy(dpBig[1])

    maxi = max(dpBig[1])
    mini = min(dpSmall[1])
print(maxi,mini)