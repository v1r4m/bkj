t = int(input())
for i in range(t):
    now, goal = map(int, input().split())
    # 1 2 3 3 3 3 2 1 이런 형태가 제일 좋음
    # 즉, 
    # 3 -> 1 1 1
    # 4 -> 1 2 1
    # 5 -> 1 2 1 1
    # 6 -> 1 2 2 1
    # 7 -> 1 2 2 1 1
    # 8 -> 1 2 2 2 1
    # 9 -> 1 2 3 2 1
    # 10 -> 1 2 3 2 1 1
    # 11 -> 1 2 3 2 2 1
    # 12 -> 1 2 3 3 2 1
    # 13 -> 1 2 3 3 2 1 1
    # ...
    # 그러면 1 2 1 , 1 2 3 2 1 이런 pivot 숫자를 알아야 하는듯?!! 
    # arr[1] = 1 -> 1개 
    # arr[2] = 4 -> 3개
    # arr[3] = 9 -> 5개
    # arr[4] = 16 # 1 2 3 4 3 2 1 -> 7개
    # n의 제곱이면 n * 2 - 1개
    diff = goal - now
    # diff에서 가장 가까운 제곱수를 찾아야 함
    sqrt_diff = diff ** 0.5
    if diff == 2:
        print(2)
    else:
        if(int(sqrt_diff) == sqrt_diff):
            print(int(sqrt_diff) * 2 - 1)
        else:
            previous_start = (int(sqrt_diff) * 2 - 1)
            next_start = ((int(sqrt_diff) + 1) * 2 - 1)
            middle = (previous_start + next_start) / 2 
            if(sqrt_diff*2 -1  > middle):
                print(int(sqrt_diff) * 2 + 1)
            else:
                print(int(sqrt_diff) * 2)