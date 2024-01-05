# def a(n):
#     result = 1
#     for i in range(n):
#         result = result * i+1
#     return result

# n = 4
# if n//2 == 0:
#     #4C2+4C4
#     #nC2+nC4+...+nCn
# else:
#     # 5!/2!*2!*1!
#     print(a(n+1))
#     pass

# 위는 실패

def dp(n):
    result1 = 0
    result2 = 1
    for i in range(1,n+1):
        result3 = result1+result2
        result1 = result2
        result2 = result3
    return result3


n = 4
print(dp(n))
    
    
