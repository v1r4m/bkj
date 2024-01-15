a, b = map(int,input().split())
def str_to_list(string):
    return [int(i) for i in string]
arr = []
for i in range(a):
    arr.append(str_to_list(input()))

# a, b = 4, 4
# arr = [[0,0,1,0],
#        [1,1,1,0],
#        [0,1,1,1],
#        [0,1,0,0]]

def recursive(x,y,dimension):
    next_dimension = dimension + 1
    if x+1 >= a or y+1 >= b:
        return dimension
    if next_dimension > min(a,b):
        return dimension
    for i in range(next_dimension):
        if arr[x+1-i][y+1] == 0:
            return dimension
    for i in range(next_dimension):
        if arr[x+1][y+1-i] == 0:
            return dimension
    #다 통과하면
    return recursive(x+1,y+1,next_dimension)

result = 0
i ,j = 0, 0
a_optimistic = a
b_optimistic=b
while i<a_optimistic:
    while j<b_optimistic:
        if arr[i][j] == 1:
            r = recursive(i,j,1)
            if r>result:
                result = r
                a_optimistic = a - result
                b_optimistic = b - result
        j+=1
    i+=1
    j=0

print(result*result)
