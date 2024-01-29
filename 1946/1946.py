t = int(input())
for i in range(t):
    n = int(input())
    #s = 서류
    #m = 면접
    #서류에서 위에있는사람들을 보고 그사람이나보다 면접점수가 떨어지는지 검사한다
    #면접에서 위에있는 사람들을 보고 그사람이 나보다 서류점수가 떨어지는지 검사한다
    #그러면, 인덱스로 접근해서,
    #s[3]=18 3번 순위의 사람은 18번 인덱스의 사람이다 이렇게 생긴 배열과
    #mi[18]=24 18번 인덱스의 사람은 m점수가 24등이라는 배열이 필요하다.
    s = [0]*(n+1)
    m = [0]*(n+1)
    si = [0]*(n+1)
    mi = [0]*(n+1)
    sm = [0]*(n+1)
    mm = [0]*(n+1)
    for j in range(n):
        so, mo = map(int, input().split())
        s[so] = j+1
        m[mo] = j+1
        si[j+1] = so
        mi[j+1] = mo
    mm[1]=mi[s[1]]
    sm[1]=si[m[1]]
    #mm[3]=2 면접이 3등이면 그 위의 최고 서류점수는 2위다
    for j in range(2,n+1): #1등부터
        sm[j]=min(sm[j-1],m[si[j]])
        mm[j]=min(mm[j-1],s[mi[j]])
    total = 0
    for j in range(1,n+1):
        sj = si[j]
        mj = mi[j]
        if sj>mm[mj] and mj>sm[sj] and sj!=1 and mj!=1: #상위호환이 있다
            total = total+1 #불합격
    print(n-total)

    