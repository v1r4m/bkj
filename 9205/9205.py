from collections import deque
def cal(p):
    for i in range(len(p)):
        pivotx, pivoty = p[i]
        flag = 1
        for j in range(len(p)):
            currx, curry = p[j]
            if i != j:
                if abs(currx-pivotx)+abs(curry-pivoty)>1000:
                    pass
                else: # 하나라도 가까운아이가있으면
                    flag = 0
                    break
        if flag:
            return "sad"
    return "happy"

t = int(input())
for i in range(t):
    n = int(input())
    hx, hy = map(int, input().split())
    p = deque()
    for i in range(n):
        tempx, tempy = map(int, input().split())
        p.append((tempx, tempy))
    px, py = map(int, input().split())
    rmlist = []
    for i in range(n):
        pivotx, pivoty = p[i]
        flag = 1
        for j in range(n):
            currx, curry = p[j]
            if abs(currx-pivotx)+abs(curry-pivoty)>1000:
                pass
            else: # 하나라도 가까운아이가있으면
                flag = 0
                break
        if flag:
            rmlist.append(i)
    rmlist.sort(reverse=True) #인덱스가 영향을 줄까봐 거꾸로 지움
    for index in rmlist:
        del p[index]
    p.insert(0, (hx, hy))
    p.append((px, py))
    print(cal(p))

    
