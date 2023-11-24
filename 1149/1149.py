n = int(input())
arr = []
for _ in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)
# n = 3
# arr = [[26, 40, 83], [49, 60, 57], [13, 89, 99]]
# r, g, b 세개밖에 없으니까 첫 페인팅을 R, G, B로 한 세가지 세계선을 생각하면 될것같은데.
# 이를테면
# 1 100 100
# 100 3 5
# 200 1 200
# 이런거일수도 있으니 그리디하게는 못한다

# 그렇다면 가장 작은걸 고르고 안되는걸 제외해가는 알고리즘은?
# 1 100 100
# 1 2 100
# 1 5 100
# 1 10 100
# 1 - 2- 1- 10 이라 언뜻보면 만족해보이지만...

# 1 2 100
# 1 30 100
# 1 5 100
# 1 10 100
#이런 반례가 있으므로 이것도 안됨

# 그렇다면 직관적으로 아니고 수학적으로 생각해보면
# BFS가 있을텐데

# tree = {}
# enum = [0,1,2]
# for i in range(n-1):
#     for j in range(3):
#         tree[(i,j)]=[(i+1,enum[(j-1)%3]),(i+1,enum[(j+1)%3])]

# from queue import Queue
# # 초기 상태
# start_node = (0, 0, 0)
# queue = Queue()
# queue.put(start_node)
# visited = [[0 for _ in range(3)] for _ in range(n)]
# sum = []

# # BFS 수행
# while not queue.empty():
#     current_node = queue.get()
#     i, j, current_cost = current_node
#     cost = current_cost+arr[i][j]
#     # 이웃한 노드를 큐에 추가
#     if i!=(n-1):
#         next = tree[(i,j)]
#         nextI, nextJ = next[0]
#         if visited[nextI][nextJ]==0:
#             queue.put((nextI, nextJ, cost))
#             visited[nextI][nextJ]=1
#         nextI, nextJ = next[1]
#         if visited[nextI][nextJ]==0:
#             queue.put((nextI, nextJ, cost))
#             visited[nextI][nextJ]=1
#     else:
#         sum.append(cost)
# print(min(sum))
def min_cost(n, costs):
    dp = [[0] * 3 for _ in range(n)]
    dp[0] = costs[0]

    for i in range(1, n):
        dp[i][0] = costs[i][0] + min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = costs[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = costs[i][2] + min(dp[i - 1][0], dp[i - 1][1])
    return min(dp[-1])

result = min_cost(n, arr)
print(result)