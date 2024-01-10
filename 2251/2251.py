# a, b, c = map(int, input().split())

# #6개의 경로를 가진 BFS

# array = []
# # 1 3 100
# # c, b, a를 추가하되 그 결과값이 c-b보다 커야 한다
# enum = [c-a, c-b, a,b,c]

# if a>=b>=c:
#     array.append(c)
#     array.append(0)
# elif b>=a>=c:
#     array.append(c)
#     array.append(0)
# elif a>=c>=b: # 100 1 3
#     array.append(c)
#     array.append(c-b)
# elif b>=c>=a: # 1 100 3
#     array.append(c)
#     array.append(c-a)
#     array.append(a)
#     array.append(0)
# else:
#     for i in range(5):
#         if enum[i]>=c-b and enum[i]<=c:
#             array.append(enum[i])
# # 3 7 7 
# array.sort()

# for i in range(len(array)):
#     print(array[i], end=' ')

a, b, c = map(int, input().split())
stack = [[0,0,c]]
visited = [[0,0,c]]
while stack:
    x, y, z = stack.pop()
    #c->b
    if z+y >= b:
        if [x,b, z-b+y] not in visited:
            visited.append([x,b, z-b+y])
            stack.append([x,b,z-b+y])
    if z+y < b:
        if [x,z+y,0] not in visited:
            visited.append([x,z+y,0])
            stack.append([x,z+y,0])
    #c->a
    if z+x >= a:
        if [a,y, z-a+x] not in visited:
            visited.append([a,y, z-a+x])
            stack.append([a,y,z-a+x])
    if z+x < a:
        if [z+x,y,0] not in visited:
            visited.append([z+x,y,0])
            stack.append([z+x,y,0])
    #b->a
    if y+x >= a:
        if [a,y+x-a,z] not in visited:
            visited.append([a,y+x-a,z])
            stack.append([a,y+x-a,z])
    if y+x < a:
        if [y+x,0,z] not in visited:
            visited.append([y+x,0,z])
            stack.append([y+x,0,z])

    #b->c
    if y+z >= c:
        if [x,y+z-c,c] not in visited:
            visited.append([x,y+z-c,c])
            stack.append([x,y+z-c,c])
    if y+z < c:
        if [x,0,y+z] not in visited:
            visited.append([x,0,y+z])
            stack.append([x,0,y+z])

    #a->b
    if x+y >= b:
        if [x+y-b,b,z] not in visited:
            visited.append([x+y-b,b,z])
            stack.append([x+y-b,b,z])
    if x+y < b:
        if [0,x+y,z] not in visited:
            visited.append([0,x+y,z])
            stack.append([0,x+y,z])

    #a->c
    if x+z >= c:
        if [x+z-c,y,c] not in visited:
            visited.append([x+z-c,y,c])
            stack.append([x+z-c,y,c])
    if x+z < c:
        if [0,y,x+z] not in visited:
            visited.append([0,y,x+z])
            stack.append([0,y,x+z])
array = []

for i in range(len(visited)):
    if visited[i][0] == 0:
        array.append(visited[i][2])

array.sort()
for i in range(len(array)):
    print(array[i], end=' ')