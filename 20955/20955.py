from sys import stdin as s

s = open("20955/input.txt", "rt")
n, m = map(int, s.readline().split())

# 인접 리스트 초기화
snaps = [[] for _ in range(n + 1)]

a, b = map(int, s.readline().split())
snaps[a].append(b)
snaps[b].append(a)

for _ in range(2, m + 1):
    a, b = map(int, s.readline().split())
    snaps[a].append(b)
    snaps[b].append(a)

visited = [False] * (n + 1)

def dfs(node):
    stack = [node]
    visited[node] = True
    node_count = 0  # 해당 컴포넌트에 포함된 노드 수
    edge_count = 0  # 해당 컴포넌트에 포함된 간선 수

    while stack:
        current = stack.pop()
        node_count += 1
        for neighbor in snaps[current]:
            edge_count += 1
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
    
    edge_count //= 2
    return node_count, edge_count

extra_edges = 0  
connected_components = 0

for i in range(1, n + 1):
    if not visited[i]:
        node_count, edge_count = dfs(i)
        extra_edges += edge_count - (node_count - 1)
        connected_components += 1

extra_edges += connected_components - 1

print(extra_edges)
