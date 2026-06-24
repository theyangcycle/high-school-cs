from collections import defaultdict
a = defaultdict(int)
b = defaultdict(int)
c = defaultdict(int)
d = defaultdict(int)
n = int(input())
for i in range(n):
    q = list(map(int,input().split()))
    if n <= 250000:
        if q[0] == 0:
            a[q[1]] = q[2]
        else:
            print(a[q[1]])
    elif n <= 500000:
        if q[0] == 0:
            b[q[1]] = q[2]
        else:
            print(b[q[1]])
    elif n <= 750000:
        if q[0] == 0:
            c[q[1]] = q[2]
        else:
            print(c[q[1]])
    else:
        if q[0] == 0:
            d[q[1]] = q[2]
        else:
            print(d[q[1]])