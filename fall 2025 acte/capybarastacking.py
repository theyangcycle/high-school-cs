a  = int(input())
for b in range(a):
    temp = list(map(int,input().split()))
    temp2 = []
    x = []
    boo = True
    for i in range(len(temp)):
        if temp[i] > temp[max(0,i-1)]:
            x.append(temp2)
            temp2 = []
            temp2.append(temp[i])
        else:
            temp2.append(temp[i])
    x.append(temp2)
    for i in x:
        if len(i) != len(set(i)):
            boo = False
    for j in range(1,len(x)):
        if sum(x[j]) >= sum(x[j-1]):
            boo = False
    if boo:
        print('VALID')
    else:
        print('INVALID')