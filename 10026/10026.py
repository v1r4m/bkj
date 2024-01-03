a = int(input())
array = []
# RRRBB
# GGBBB
# BBBRR
# BBRRR
# RRRRR
for i in range(a):
    temp = list(input())
    array.append(temp)
# a = 5

# array = [['R','R','R','B','B'],
#          ['G','G','B','B','B'],
#         ['B','B','B','R','R'],
#         ['B','B','R','R','R'],
#         ['R','R','R','R','R']]


visited = [[1 for _ in range(a)] for _ in range(a)]

stack = []
def popVisited(visited, x, y):
    for i in range(a):
        for j in range(a):
            if visited[i][j]:
                return (i,j)
    return (-1,-1)
count = 0
check = popVisited(visited, 0, 0)
while check!=(-1,-1):
    x, y = check
    visited[x][y] = 0
    stack.append([x,y,array[x][y]])
    while (stack):
        x, y, color = stack.pop()
        if x+1 < a and array[x+1][y] == color and visited[x+1][y]:
            visited[x+1][y] = 0
            stack.append([x+1, y, array[x+1][y]])
        if y+1 < a and array[x][y+1] == color and visited[x][y+1]:
            visited[x][y+1] = 0
            stack.append([x, y+1, array[x][y+1]])
        if x-1 >= 0 and array[x-1][y] == color and visited[x-1][y]:
            visited[x-1][y] = 0
            stack.append([x-1, y, array[x-1][y]])
        if y-1 >= 0 and array[x][y-1] == color and visited[x][y-1]:
            visited[x][y-1] = 0
            stack.append([x, y-1, array[x][y-1]])
    count += 1
    check = popVisited(visited, x, y)
acount = count

visited = [[1 for _ in range(a)] for _ in range(a)]
for i in range(a):
    for j in range(a):
        if array[i][j] == 'G':
            array[i][j] = 'R'
count = 0
check = popVisited(visited, 0, 0)
while check!=(-1,-1):
    x, y = check
    stack.append([x,y,array[x][y]])
    visited[x][y] = 0
    while (stack):
        x, y, color = stack.pop()
        if x+1 < a and array[x+1][y] == color and visited[x+1][y]:
            visited[x+1][y] = 0
            stack.append([x+1, y, array[x+1][y]])
        if y+1 < a and array[x][y+1] == color and visited[x][y+1]:
            visited[x][y+1] = 0
            stack.append([x, y+1, array[x][y+1]])
        if x-1 >= 0 and array[x-1][y] == color and visited[x-1][y]:
            visited[x-1][y] = 0
            stack.append([x-1, y, array[x-1][y]])
        if y-1 >= 0 and array[x][y-1] == color and visited[x][y-1]:
            visited[x][y-1] = 0
            stack.append([x, y-1, array[x][y-1]])
    count += 1
    check=popVisited(visited, x, y)
bcount = count

print(acount, bcount)