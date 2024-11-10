from sys import stdin as s

s = open("20955/input.txt", "rt")
n, m = map(int, s.readline().split())
snaps = [[False for _ in range(n+1)] for _ in range(n+1)]
a,b = map(int, s.readline().split())
snaps[a][b]=True
snaps[b][a]=True
root = a
root_connected = [False for _ in range(n+1)]
root_connected[root]=True
for i in range(2,m+1):
    a,b = map(int, s.readline().split())
    snaps[a][b]=True
    snaps[b][a]=True
traverse = []
for i in range(n+1):
    if snaps[root][i]:
        traverse.append((i,root))
work = 0
flag = 1
while flag:
    while traverse:
        next_traverse, before_traverse = traverse.pop()
        if root_connected[next_traverse]:#visited
            work=work+1
        else:#good
            for i in range(n+1):
                if snaps[next_traverse][i] and i != before_traverse:
                    traverse.append((i,next_traverse))
                root_connected[next_traverse]=True
    for i in range(1,n+1):
        if root_connected[i]==False:
            work = work+1
            #attach root and i
            root_connected[i]=True
            traverse.append((i,root))
            break
        else:
            flag=0
print(work)
