from collections import deque
import sys
sys.setrecursionlimit(10**5)

n,root,question = map(int,input().split())
arr = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

root_arr = [[] for i in range(n+1)]
deq = deque()
for i in range(len(arr[root])):
    deq.append([root,arr[root][i]])
while deq:
    a,b = deq.popleft() # 보장되어있는 애들
    root_arr[a].append(b)
    for i in range(len(arr[b])):
        if arr[b][i] != a:
            deq.append([b,arr[b][i]])
minimum = [0 for _ in range(n+1)]

def countSubtreeNodes(currentNode):
    minimum[currentNode] = 1 
    for Node in root_arr[currentNode]:
        countSubtreeNodes(Node)
        minimum[currentNode] += minimum[Node]

countSubtreeNodes(root)

# stack = []
# for i in range(len(root_arr[root])):
#     stack.append([root,root_arr[root][i]])

# while stack:
#     a,b= stack.pop()
#     mul = 1
#     plus = 0
#     for i in range(len(root_arr[b])):
#         mul = mul * minimum[root_arr[b][i]]
#         if minimum[root_arr[b][i]]:
#             plus = plus + minimum[root_arr[b][i]]
#     if len(root_arr[b]) == 0:
#         minimum[b] = 1
#     elif mul != 0:
#         if minimum[b] == 0:
#             minimum[b] = plus + 1
#         else:
#             for i in range(len(root_arr[a])):
#                 mul = mul * minimum[root_arr[a][i]]
#                 if minimum[root_arr[a][i]]:
#                     plus = plus + minimum[root_arr[a][i]]
#             if mul!=0:
#                 minimum[a]=plus + 1
#     else:
#         stack.append([a,b])
#         for i in range(len(root_arr[b])):
#             stack.append([b,root_arr[b][i]])
# minimum[root] = n

for i in range(question):
    a = int(input())
    print(minimum[a])