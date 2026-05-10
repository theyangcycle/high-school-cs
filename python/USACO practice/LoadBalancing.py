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
xvals,yvals = sorted(xvals),sorted(yvals)
for i in range(len(xvals)-2):
    a = xvals[i]+1
    for j in range(len(yvals)-2):
        b = yvals[j]+1
        temp = []
        count = 1
        for k in range(len(cows)):
            if cows[k][0]<a and cows[k][1]<b:
                count += 1
        temp.append(count)
        count = 0
        for k in range(len(cows)):
            if cows[k][0]<a and cows[k][1]>b:
                count += 1
        temp.append(count)
        count = 0
        for k in range(len(cows)):
            if cows[k][0]>a and cows[k][1]<b:
                count += 1
        temp.append(count)
        count = 0
        for k in range(len(cows)):
            if cows[k][0]>a and cows[k][1]>b:
                count += 1
        temp.append(count)
        m.append(max(temp))
print(min(m))