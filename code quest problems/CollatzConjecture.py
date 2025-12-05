a=int(input())
for b in range(a):
    x=int(input())
    z=x
    y=[]
    while x != 1:
        y.append(int(x))
        if x % 2 == 0:
            x = x/2
        else:
            x = x*3+1
    y.append(int(x))
    print(y)
    print(str(z)+":"+str(len(y)))