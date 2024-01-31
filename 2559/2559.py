n,m = map(int,input().split())
arr = list(map(int,input().split()))
train = 0
for i in range(m):
    train = train + arr[i]
max = train
for i in range(n-m):
    train = train - arr[i] + arr[i+m]
    if max<train:
        max = train
print(max)