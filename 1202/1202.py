import heapq

n,k = map(int,input().split())
gem = []
for i in range(n):
    gemW, gemV = map(int,input().split())
    gem.append([-1*gemW,-1*gemV])
bagWeight = []
for i in range(k):
    bagWeight.append(int(input()))
gem.sort()
gem.reverse()
bagWeight.sort()
bagWeight.reverse()
bag = []
heapq.heapify(bag)#최소
gemIndex = 0
bagIndex = 0
heapq.heapify(gem)#최대
while len(gem) and bagIndex<k:
    gemW, gemV = heapq.heappop(gem)
    gemW = gemW * -1
    gemV = gemV * -1
    if bagWeight[bagIndex]<gemW:#안들어가면
        #없애버림
        #..
        if len(bag):
            if bag[0][0]<gemV:#위에는 당연히 들어감. 그런데 바꿀 가치가 있으면
                heapq.heappop(bag)
                heapq.heappush(bag,[gemV, gemW])
                #bagIndex값은 올라가지 않음(바꿧으므로)
    else:#만약에 들어가면
        #걍 넣어버림
        heapq.heappush(bag,[gemV,gemW])
        bagIndex = bagIndex + 1
#마지막으로 bagIndex = k 인것 계산함
while len(gem):
    gemW, gemV = heapq.heappop(gem)
    gemW = gemW * -1
    gemV = gemV * -1
    if bag[0][0]<gemV:#위에는 당연히 들어감. 그런데 바꿀 가치가 있으면
        heapq.heappop(bag)
        heapq.heappush(bag,[gemV, gemW])

total = 0
for i in range(len(bag)):
    total = total+bag[i][0]
print(total)

    