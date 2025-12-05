a = int(input())
for b in range(a):
    lastyr = input().split(',')
    thisyr = input().split(',')
    onezero = []
    oneone = []
    zeroone=[]
    for i in range(len(lastyr)):
        if lastyr[i] not in thisyr:
            onezero.append(lastyr[i])
        else:
            oneone.append(lastyr[i])
    for i in range(len(thisyr)):
        if thisyr[i] not in lastyr:
            zeroone.append(thisyr[i])
    onezero.sort(),oneone.sort(),zeroone.sort()
    onezero = ','.join(onezero)
    oneone = ','.join(oneone)
    zeroone = ','.join(zeroone)
    print(onezero)
    print(oneone)
    print(zeroone)