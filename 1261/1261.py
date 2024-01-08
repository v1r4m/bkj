from collections import deque

b, a = map(int, input().split())
array = []
value = []
for i in range(a):
    temp = list(input())
    valueTemp = [float('inf') for _ in range(b)]
    value.append(valueTemp)
    array.append(temp)
stack = deque()
stack.append([0,0,0])
value[0][0] = 0
result = 0
x = 0
y = 0
while stack:
    x, y, v = stack.popleft()
    if x+1 < a and value[x+1][y] > v:
        if array[x+1][y] == '0':
            stack.append([x+1,y,v])
            value[x+1][y] = v
        elif value[x+1][y] > v+1:
            stack.append([x+1,y,v+1])
            value[x+1][y] = v+1
    if y+1 < b and value[x][y+1] > v:
        if array[x][y+1] == '0':
            stack.append([x,y+1,v])
            value[x][y+1] = v
        elif value[x][y+1] > v+1:
            stack.append([x,y+1,v+1])
            value[x][y+1] = v+1
    if x-1 >= 0 and value[x-1][y] > v:
        if array[x-1][y] == '0':
            stack.append([x-1,y,v])
            value[x-1][y] = v
        elif value[x-1][y] > v+1:
            stack.append([x-1,y,v+1])
            value[x-1][y] = v+1
    if y-1 >= 0 and value[x][y-1] > v:
        if array[x][y-1] == '0':
            stack.append([x,y-1,v])
            value[x][y-1] = v
        elif value[x][y-1] > v+1:
            stack.append([x,y-1,v+1])
            value[x][y-1] = v+1
print(value[a-1][b-1])