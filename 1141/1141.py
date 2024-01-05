n = int(input())
array = []
for i in range(n):
    array.append(input())
array.sort(key=lambda x: (len(x), x)) #일단 소팅을 하고...
result = 0
for i in range(n):
    flag = True
    for j in range(i+1,n):
        if array[i] == array[j][:len(array[i])]:
            flag=False
            break
    if flag:
        result = result + 1
print(result)