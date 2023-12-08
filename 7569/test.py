a, b, c = map(int,input().split())
arr = [[[0 for _ in range(a)] for _ in range(b)] for _ in range(c)]
for i in range(c):
    for j in range(b):
        arr[i][j] = list(map(int,input().split())) #a개
# a, b, c = 5, 3, 2
# arr = [[[0,0,0,0,0],
#         [0,0,0,0,0],
#         [0,0,0,0,0]],
#         [[0,0,0,0,0],
#         [0,0,1,0,0],
#         [0,0,0,0,0]]]

# a,b,c=5,3,1
# arr = [[[0,-1,0,0,0],
#         [-1,-1,0,1,1],
#         [0,0,0,1,1]]]

stack = []
nextStack = []

for i in range(c):
    for j in range(b):
        for k in range(a):
            if arr[i][j][k]==1:
                stack.append([i,j,k])

turn = 0

while True:
    while stack:
        z,y,x = stack.pop()
        #enum으로 처리해도 되지만 헷갈리니까 그냥...
        #상
        if y+1<b and arr[z][y+1][x]==0:
            arr[z][y+1][x]=1
            nextStack.append([z,y+1,x])
        #하
        if y-1>=0 and arr[z][y-1][x]==0:
            arr[z][y-1][x]=1
            nextStack.append([z,y-1,x])
        #좌
        if x+1<a and arr[z][y][x+1]==0:
            arr[z][y][x+1]=1
            nextStack.append([z,y,x+1])
        #우
        if x-1>=0 and arr[z][y][x-1]==0:
            arr[z][y][x-1]=1
            nextStack.append([z,y,x-1])
        #위
        if z+1<c and arr[z+1][y][x]==0:
            arr[z+1][y][x]=1
            nextStack.append([z+1,y,x])
        #아래
        if z-1>=0 and arr[z-1][y][x]==0:
            arr[z-1][y][x]=1
            nextStack.append([z-1,y,x])
    turn = turn + 1
    if nextStack == []:
        for i in range(c):
            for j in range(b):
                for k in range(a):
                    if arr[i][j][k]==0:
                        turn = 0
        print(turn-1)
        break
    stack = nextStack
    nextStack = []