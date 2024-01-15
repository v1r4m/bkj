import random



def gibiee(n,m,nums):

    dp = [[0] * m for _ in range(n)]

    for i in range(n) :
        for j in range(m) :
            able = dp[i][j]
            while True :
                able += 1
                if n-i < able or m-j < able : break

                state = True
                row = i + (able-1)
                for idx in range(j, j+able) :
                    if nums[row][idx] == 0 :
                        state = False
                        break

                if state == False : break

                col = j + (able-1)
                for idx in range(i, i+able) :
                    if nums[idx][col] == 0 :
                        state = False
                        break

                if state == False : break

                for ii in range(i, i+able) :
                    for jj in range(j, j+able) :
                        if dp[ii][jj]+1 > m-jj : continue
                        elif dp[ii][jj]+1 > n-ii : continue 
                        else : dp[ii][jj] += 1

    answer = 0
    for i in range(n) :
        answer = max(answer, max(dp[i]))

    return answer * answer


def viram(a,b,arr):
    result = 0
    i ,j = 0, 0
    a_optimistic = a
    b_optimistic=b
    while i<a_optimistic:
        while j<b_optimistic:
            if arr[i][j] == 1:
                r = recursive(i,j,1,a,b,arr)
                if r>result:
                    result = r
                    a_optimistic = a - result
                    b_optimistic = b - result
            j+=1
        i+=1
        j=0

    return result*result

def recursive(x,y,dimension,a,b,arr):
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
    return recursive(x+1,y+1,next_dimension,a,b,arr)



while True:
    n = 4
    m = 4
    nums = [[random.randint(0,1) for _ in range(m)] for _ in range(n)]
    if gibiee(n,m,nums) != viram(n,m,nums):
        print(nums)
        print(gibiee(n,m,nums), viram(n,m,nums))
        break



