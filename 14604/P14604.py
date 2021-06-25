import numpy as np

number = int(input())
feature=np.zeros([number,3])

for i in range(number):
    temp = input().split(" ")
    if temp[2]=="LOVELIYZ":
        temp[2]=1
    else:
        temp[2]=0
    feature[i]=temp
