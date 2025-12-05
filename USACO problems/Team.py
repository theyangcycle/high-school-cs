a = int(input())
count = 0
for b in range(a):
    x = list(map(int,input().split()))
    if sum(x) >= 2:
        count += 1
print(count)