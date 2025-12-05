a = int(input())
for b in range(a):
    n = int(input())
    name = []
    type = []
    xval = []
    yval = []
    
    for i in range(n): # puts each input in to 4 seperate lists
        inp = input().split(':')
        inp0 = inp[0].split('_')
        inp1 = inp[1].split(',')
        name.append(inp0[0])
        type.append(inp0[1])
        xval.append(inp1[0])
        yval.append(inp1[1])
    
    xval = list(map(int,xval))
    yval = list(map(int,yval))
    
    # sorts lists by decreasing order for yval
    paired = list(zip(yval, name, type, xval))
    paired.sort(reverse=True)
    yval, name, type, xval = zip(*paired)
    name, type, xval, yval = list(name), list(type), list(xval), list(yval)

    for j in range(n): # destroys ships
        x = xval.index(min(xval))
        print(f"Destroyed Ship: {name[x]} xLoc: {xval[x]}")
        name.pop(x)
        type.pop(x)
        xval.pop(x)
        yval.pop(x)
        for k in range(len(type)):
            if type[k] == 'A':
                xval[k] -= 10
            elif type[k] == 'B':
                xval[k] -= 20
            elif type[k] == 'C':
                xval[k] -= 30