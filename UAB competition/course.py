n = int(input())
x = int(input())
a = []
b = []
c = 0
if n != 1:
    for y in range(x):
        z = input().split()
        a.append(z[0])
        b.append(z[1])
    while c < len(b):
        if b[0] in a:
            b.pop(0)
        else:
            c+=1
    if len(b) == 0:
        print(0)
    else:
        print(1)
else:
    print(1)