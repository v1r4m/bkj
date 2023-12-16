from collections import deque

def cal(stack, p, visited, px, py):
    while stack:
        pivotx, pivoty, pivotindex = stack.popleft()
        for j in range(len(p)):
            nextx, nexty = p[j]
            if abs(nextx-pivotx)+abs(nexty-pivoty) <=1000 and visited[j]==0:
                visited[j] = 1
                stack.append((nextx, nexty, j))
                if (nextx, nexty) == (px, py):
                    return("happy")
    return("sad")

t = int(input())
for i in range(t):
    n = int(input())
    hx, hy = map(int, input().split())
    p = []
    for j in range(n):
        tempx, tempy = map(int, input().split())
        p.append((tempx, tempy))
    px, py = map(int, input().split())
    if n == 0:
        if abs(hx-px)+abs(hy-py)<=1000:
            print("happy")
        else:
            print("sad")
    else:
        if abs(hx-px)+abs(hy-py)<=1000:
            print("happy")
        else:
            stack = deque()
            visited = [0 for j in range(n+1)]

            for j in range(n):
                pivotx, pivoty = p[j]
                if abs(hx-pivotx)+abs(hy-pivoty)<=1000:
                    stack.append((pivotx,pivoty,j))

            p.append((px,py))
            print(cal(stack, p, visited, px, py))