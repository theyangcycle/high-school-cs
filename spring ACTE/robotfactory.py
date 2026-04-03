n = int(input())
knum = int(input())
k = list(map(int,input().split()))
count = 0
for i in range(1,n+1):
    for j in k:
        if j == 0:
            continue
        if i%j == 0:
            count+=1
            break
print(count)