from sys import stdin as s

s = open("1013/input.txt", "rt")

n = int(s.readline())

#100+1+|01
def checkNow(status, string):
    if status == 0:
        if string == '1':
            return 2
        else:
            return 1
    elif status == 1:
        if string == '1':
            return 0
        else:
            return 'FAIL'
    elif status == 2:
        if string == '1':
            return 'FAIL'
        else:
            return 3
    elif status == 3:
        if string == '1':
            return 'FAIL'
        else:
            return 4
    elif status == 4:
        if string == '1':
            return 5
        else:
            return 4
    elif status == 5:
        if string == '1':
            return 6
        else:
            return 8
    elif status == 6:
        if string == '1':
            return 6
        else:
            return 7
    elif status == 7:
        if string == '1':
            return 0
        else:
            return 4
    elif status == 8:
        if string == '1':
            return 0
        else:
            return 'FAIL'
    

for i in range(n):
    input = s.readline().strip()
    status = 0
    for j in range(len(input)):
        next = checkNow(status, input[j])
        if next == 'FAIL':
            status = next
            print('NO')
            break
        else:
            status = next
    if status == 5 or status == 6 or status == 0:
        print('YES')
    elif status != 'FAIL':
        print('NO')