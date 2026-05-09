n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
dist = []
for i in range(n):
    for j in range(i+1,n):
        dist.append((abs(x[i]-x[j])**2)+(abs(y[i]-y[j])**2))
print(max(dist))