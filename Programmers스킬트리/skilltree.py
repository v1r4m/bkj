# a = input()
# b = map(list, input().split())
from collections import deque

a = "CBD"
b = ["BACDE", "CBADF", "AECB", "BDA"]
alist = deque() #queue
list = []

for i in range(len(a)):
    alist.append(a[i])
    list.append(a[i])

blist = alist.copy()

result = 0

for item in b:
    current = alist.popleft()
    for i in range(len(item)):
        if item[i] in list:
            if item[i] == current:
                if len(alist) == 0:
                    break
                current = alist.popleft()
                pass
            else:
                result = result - 1
                break
    result = result + 1
    alist = blist.copy()

print(result)

