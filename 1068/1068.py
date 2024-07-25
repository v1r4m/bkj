from sys import stdin as s

s = open("1068/input.txt", "rt")

def traverse(tree, node):
    if len(tree[node])==0:
        return 1
    else:
        a = 0
        for i in range(len(tree[node])):
            a += traverse(tree, tree[node][i])
        return a
    
n = int(s.readline())
arr = list(map(int, s.readline().split()))
remove = int(s.readline())
tree = [[] for _ in range(n)]
root = -1
for i in range(n):
    if arr[i] == -1:
        root = i
    else:
        tree[arr[i]].append(i)
if remove == root:
    print(0)
else:
    for i in range(n):
        for j in range(len(tree[i])):
            if tree[i][j] == remove:
                tree[i].remove(tree[i][j])
                break #트리는 싸이클이 없으므로 여기서 멈춰두 댄당..

    print(traverse(tree,root))

