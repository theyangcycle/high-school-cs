def lunar(val):
    return val-180

a=int(input())
for b in range(a):
    x=input().split(' ')
    x=list(map(float,x))
    
    x=list(map(lunar,x))

    for y in range(len(x)):
        if x[y] < 0:
            x[y] = 360+x[y]

    for num in range(len(x)):
        x[num]=round(x[num],2)
    
    for z in range(len(x)):
        if x[z] < 10:
            x[z] = str(x[z])
            x[z] = x[z].ljust(4,'0')
            x[z] = x[z].rjust(6,'0')
        elif x[z] < 100:        
            x[z] = str(x[z])
            x[z] = x[z].ljust(5,'0')
            x[z] = x[z].rjust(6,'0')
        else:
            x[z] = str(x[z])
            x[z] = x[z].ljust(6,'0')
    
    x=' '.join(x)
    print(x)