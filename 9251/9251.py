from sys import stdin as s

s = open("9251/input.txt", "rt")

arr1, arr2 = s.read().splitlines()

len1 = len(arr1)
len2 = len(arr2)
index1 = []
index2 = []

for i in range(len1):
    index1.append(i)
for i in range(len2):
    index2.append(i)

from itertools import combinations
start1 = combinations(index1,2)
start2 = combinations(index2,2)
nextstart1 = []
nextstart2 = []

for i in range(len(start1)):#정렬로 이 과정을 좀 더 빠르게 할 수 없을까..
    for j in range(len(start2)):
        for k in range(len(start1[i])):
            if arr1[start1[i][k]]!=arr2[start2[j][k]]:
                break
            else: #같으면
                if k == len(start1[i])-1:
                    nextstart1.append(start1[i])
                    nextstart2.append(start2[i])
                    



print(nextstart1, nextstart2)