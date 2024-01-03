#A B C D E F
#0 1 2 3 4 5

#ABD
#ABC
#ADE
#ACE
#FDB
#FBC
#FDE
#FCE

#AD
#AB
#AC
#AE
#DB
#BC
#CE
#ED
#FD
#FC
#FE
#FB

a = int(input())
array = list(map(int, input().split()))
enum3 = [[0,1,3],[0,1,2],[0,3,4],[0,2,4],[1,3,5],[1,2,5],[3,4,5],[2,4,5]]
enum2 = [[0,1],[0,2],[0,3],[0,4],[1,3],[1,2],[2,4],[3,4],[3,5],[2,5],[4,5],[1,5]]
#1 2 3 4 5 6

# n = 2 면 3 => 4개, 2=> 4개
# n = 3 면 3 => 4개, 2=> 4+4+4개, 1 => 1+1*4+4*1개
# n = 4 면 3 => 4개, 2=> 8+8+4개, 1 => 4+4*4+4*2개
# n = 5 면 3 => 4개, 2=> 12+12+4개, 1 => 9+9*4+4*3개

# n = n 면 3 => n개, 2=> 4*(n-2)*2 + 4개, 1 => (n-2)*(n-2)+(n-2)*(n-2)*4+4*(n-2)개
# n = n 면 3 => n개, 2=> 8*(n-2)+4 개, 1=> 5(n-2)*(n-2)+4*(n-2)개

# 4 12 9
# 6 3 1
# 24 + 36 + 9 = 69
enum3max = float('inf')
enum2max = float('inf')
for i in range(len(enum3)):
    if array[enum3[i][0]]+array[enum3[i][1]]+array[enum3[i][2]] < enum3max:
        enum3max=array[enum3[i][0]]+array[enum3[i][1]]+array[enum3[i][2]]
for i in range(len(enum2)):
    if array[enum2[i][0]]+array[enum2[i][1]] < enum2max:
        enum2max=array[enum2[i][0]]+array[enum2[i][1]]
enum1max = min(array)
enum1min = max(array)

if a == 1:
    print(sum(array)-enum1min)
else:
    print(enum3max*4+enum2max*(8*(a-2)+4)+enum1max*(5*(a-2)*(a-2)+4*(a-2)))
