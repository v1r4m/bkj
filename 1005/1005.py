import sys
sys.setrecursionlimit(10**9)

a = int(input())
# a = 1

# def recursive(list, edge, rmax, cm, cursor):
#     if len(edge[cursor])==0:
#         return list[cursor]
#     for item in edge[cursor]:
#         cm = cm+recursive(list, edge, rmax, cm, item)+list[cursor]
#         if cm>rmax:
#             rmax = cm
#             cm = 0
#     return rmax

def recursive(values, edge, cursor, vs):
    if vs[cursor] != -1:
        return vs[cursor]
    if len(edge[cursor])==0:
        return values[cursor]
    cm = 0 
    for item in edge[cursor]:
        next = recursive(values, edge, item, vs)
        cm = max(cm, next)
    vs[cursor] = cm+values[cursor]
    return vs[cursor]
    # if vs[cursor]<rs:
    #     vs[cursor]=rs
    #     return rs
    # else:
    #     return 0
    

#시간초과나면 재귀에 디피를 더하기

for i in range(a):
    n,k = map(int, sys.stdin.readline().split())
    values = list(map(int, sys.stdin.readline().split()))
    values.insert(0, 0)
    edge = [[] for _ in range(n+1)]
    vs = [-1 for _ in range(n+1)]
    for j in range(k):
        a, b = map(int, sys.stdin.readline().split())
        edge[b].append(a)
    # values = [0,10,20,1,5,8,7,1,43]
    # edge = [[], [], [1], [1], [2], [2], [3], [5, 6], [7]]
    # key = 7
    key = int(input())
    ## 데이터 준비 끝 
    print(recursive(values, edge, key, vs))
    # dp = [0] * (n+1)
    # stack = deque()
    # for j in range(1, n+1):
    #     if len(edge[j])==0:
    #         stack.append(j)
    # while stack: #이렇게 늘어나는게 아니라 완전 못생기게 생긴거를 고려해야함
    #     cm = 0
    #     j = stack.pop()
    #     for next in edge[j]:
    #         cm = max(cm, dp[next])
    #     dp[j] = cm + values[j]
    #     for k in edge2[j]:
    #         if dp[k] < dp[j]+values[k]:
    #             stack.append(k)
    # print(dp[key])