n,m = map(int,input().split())
cows = []
ac = []
for _ in range(n):
    cows.append(list(map(int,input().split())))
for _ in range(m):
    ac.append(list(map(int,input().split())))
stalls = [0]*max([cows[_][1] for _ in range(len(cows))])
for i in range(len(cows)):
    stalls[cows[i][0]-1:cows[i][1]] = [cows[i][2]]*(cows[i][1]-cows[i][0]+1)

cost = float("inf")
for i in range(1,1<<m):
    sub = []
    temp = stalls[:]
    tempcost = 0
    for j in range(m):
        if i & (1<<j):
            sub.append(ac[j])
    for k in sub:
        for l in range(k[0]-1,k[1]):
            temp[l]-=k[2]
        tempcost += k[3]
    boo = True
    for k in temp:
        if k > 0:
            boo = False
            break
    if boo:
        cost = min(cost,tempcost)
print(cost)