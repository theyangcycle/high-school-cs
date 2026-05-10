n = int(input())
xvals = []
yvals = []
cows = []
m = []
for i in range(n):
    x,y = map(int,input().split())
    xvals.append(x)
    yvals.append(y)
    cows.append([x,y])
xvals,yvals = set(sorted(xvals)),set(sorted(yvals))
for a in xvals:
    a += 1
    for b in yvals:
        b += 1
        bl = br = tl = tr = 0
        for j in cows:
            if j[0]<a:
                if j[1] < b:
                    bl += 1
                else:
                    tl += 1
            elif j[0]>a:
                if j[1] < b:
                    br += 1
                else:
                    tr += 1
        m.append(max(bl,br,tl,tr))
print(min(m))