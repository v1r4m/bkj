n = int(input())
chess = [[0]*n for _ in range(n)]
#first_chess에 우선 놓고, 나머지 퀸들은 차례대로 놓고 첫 퀸(이전 퀸)과 비교하여 놓을 수 있는지 확인
#nxn 체스판에 n개의 퀸이기 때문에 한 줄에는 무조건 한 개이 체스말이 있고 그래서 [0][i]에 체스말이 있는게 보장된다. 
#다음줄로 넘어가면서 어디에 놓아야하는지 확인...왜냐하면 한 줄에는 무조건 한 개의 체스말이 있기 때문이다. 
#같은 가로줄에 퀸이 이미 있는지 확인
#같은 세로줄은 확인할 필요가 없다
#같은 대각선에 퀸이 이미 있는지 확인
#모두 만족하면 놓을 수 있음
#모든 퀸을 놓았으면 1리턴
def is_possible(x, y):
    for i in range(x):#같은 가로줄!!! 
        if chess[i][y] == 1:
            return False
    for i in range(1, x+1):
        if y-i >= 0 and chess[x-i][y-i] == 1: #위 왼쪽
            return False
        if y+i < n and chess[x-i][y+i] == 1: #아래 왼쪽
            return False
    return True
def recursive(x):
    if x == n: #모든 퀸을 놓았으면
        return 1
    cnt = 0
    for i in range(n):
        if chess[x][i] == 0 and is_possible(x, i):
            chess[x][i] = 1
            cnt = cnt+ recursive(x+1)
            chess[x][i] = 0
    return cnt
total = 0
for i in range(n):
    chess[0][i] = 1
    total = total + recursive(1)
    chess[0][i] = 0
print(total)