n = int(input())
p = list(map(int,input().split()))
differences = []
for i in range(1,2**n):
    conb = bin(i)
    group1 = []
    group2 = []
    id = 0
    for j in range(len(conb)-n,len(conb)):
        if conb[j] == '1':
            group1.append(p[id])
        else:
            group2.append(p[id])
        id+=1
    differences.append(abs(sum(group1)-sum(group2)))
print(min(differences))