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

def main():
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
        print(0)
        return

    bfs(queue)
    result = -2
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                print(-1)
                return
            else:
                result = max(result, map[i][j])

    print(result - 1)

if __name__ == "__main__":
    main()
