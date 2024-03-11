from sys import stdin as s

s = open("14499/input.txt", "rt")

n,m,currentX,currentY,commandCount = map(int,s.readline().split())
arr = []
for i in range(n):
    temp = list(map(int, s.readline().split()))
    arr.append(temp)
command = list(map(int, s.readline().split()))
dice = [0,0,0,0,0,0]
#  1
#3 0 2
#  4
#  5

#윗면이 0
#바닥은 5
#엄청 많이 돌아다니면 결국 주사위와 지도는 다 0이 없게 된다

moveDice = [
    [(0,3),(3,5),(5,2),(2,0)], #동
    [(0,2),(2,5),(5,3),(3,0)], #서
    [(0,4),(4,5),(5,1),(1,0)], #북
    [(0,1),(1,5),(5,4),(4,0)]  #남
]

for i in range(commandCount):
    if(command[i] == 1): #동
        if(currentY + 1 < m):
            currentY += 1
            top = dice[0] #현재의 윗면
            for changeFrom,changeTo in (moveDice[command[i]-1]):
                dice[changeFrom] = dice[changeTo]
            dice[2]=top
            if(arr[currentX][currentY] == 0):
                arr[currentX][currentY] = dice[5] #미래의 바닥
            else:
                dice[5] = arr[currentX][currentY]
                arr[currentX][currentY] = 0 
            print(dice[0])
    elif(command[i] == 2): #서
        if(currentY - 1 >= 0):
            currentY -= 1
            top = dice[0] #현재의 윗면
            for changeFrom,changeTo in (moveDice[command[i]-1]):
                dice[changeFrom] = dice[changeTo]
            dice[3]=top
            if(arr[currentX][currentY] == 0):
                arr[currentX][currentY] = dice[5]
            else:
                dice[5] = arr[currentX][currentY]
                arr[currentX][currentY] = 0
            print(dice[0])
    elif(command[i] == 3): #북
        if(currentX - 1 >= 0):
            currentX -= 1
            top = dice[0] #현재의 윗면
            for changeFrom,changeTo in (moveDice[command[i]-1]):
                dice[changeFrom] = dice[changeTo]
            dice[1]=top
            if(arr[currentX][currentY] == 0):
                arr[currentX][currentY] = dice[5]
            else:
                dice[5] = arr[currentX][currentY]
                arr[currentX][currentY] = 0
            print(dice[0])
    elif(command[i] == 4): #남
        if(currentX + 1 < n):
            currentX += 1
            top = dice[0] #현재의 윗면
            for changeFrom,changeTo in (moveDice[command[i]-1]):
                dice[changeFrom] = dice[changeTo]
            dice[4]=top
            if(arr[currentX][currentY] == 0):
                arr[currentX][currentY] = dice[5]
            else:
                dice[5] = arr[currentX][currentY]
                arr[currentX][currentY] = 0
            print(dice[0])
            