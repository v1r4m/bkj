n = int(input())
arr = list(map(int,input().split()))
arr.reverse()
now = 1
line = []
while len(arr) or (len(line) and line[-1])==now:
    if len(arr) and arr[-1]==now: #지금
        arr.pop()
        now = now + 1
    elif len(line) and  line[-1]==now:# 대기열
        line.pop()
        now = now + 1 
    else: # 그 어디에도 없다
        if len(arr):
            item = arr.pop()
            line.append(item)
        else: #그 어디에도없는데 대기열도 안남았다
            print('Sad')
            exit()
if len(arr) or len(line):
    print('Sad')
else:
    print('Nice')