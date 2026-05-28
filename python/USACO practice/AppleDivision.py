n = int(input())
p = list(map(int,input().split()))
differences = []
for i in range(1<<n):
    sum1 = 0
    sum2 = 0
    for j in range(n):
        if i & (1<<j):
            sum1 += p[j]
        else:
            sum2 += p[j]
    differences.append(abs(sum1-sum2))
print(min(differences))