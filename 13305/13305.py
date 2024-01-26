a = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = price[0]
total = 0
for i in range(a-1):
    if price[i] < min_price:
        min_price = price[i]
    total = total + min_price * dist[i]

print(total)