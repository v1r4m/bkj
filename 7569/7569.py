def main2():
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


from collections import deque

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def bfs(queue):
    while queue:
        node = queue.popleft()
        for i in range(6):
            nx = node.x + dx[i]
            ny = node.y + dy[i]

            if 0 <= nx < len(map[0]) and 0 <= ny < len(map):
                if map[ny][nx] == 0:
                    map[ny][nx] = map[node.y][node.x] + 1
                    queue.append(Node(nx, ny))

def main1():
    global dx, dy, map

    m, n, h = map(int, input().split())
    dx = [0, 0, -1, 1, 0, 0]
    dy = [1, -1, 0, 0, n, -n]
    map = [[0] * m for _ in range(n * h)]

    queue = deque()
    full = True

    for j in range(n * h):
        values = list(map(int, input().split()))
        for k in range(m):
            value = values[k]
            if value == 1:
                queue.append(Node(k, j))
            if value == 0:
                full = False
            map[j][k] = value

    if full:
        return 0

    bfs(queue)
    result = -2
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                return -1
            else:
                result = max(result, map[i][j])

    return result - 1
import random
if __name__ == "__main__":
    a,b,c = random.randrange(3),random.randrange(3),random.randrange(3)
    arr = [[[0 for _ in range(a)] for _ in range(b)] for _ in range(c)]
    for i in range(a):
        for j in range(b):
            for k in range(c):
                arr[a][b][c] = random.choice([0,-1,1])
    r2 = main2(a,b,c,arr)
    r1 = main1(a,b,c,arr)
    if r2!=r1:
        print(r2,r1)
        print(a,b,c)
        print(arr)
        print("error")
