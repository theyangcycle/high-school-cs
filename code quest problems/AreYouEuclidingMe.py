a = int(input())
for b in range(a):
    x=input().split(',')
    x=list(map(int, x))
    minuend=max(x)
    subtrahend=min(x)
    difference=1
    list1=[]
    while difference != 0:
        list1=[]
        difference = minuend-subtrahend
        print(str(minuend)+'-'+str(subtrahend)+'='+str(difference))
        list1.append(subtrahend)
        list1.append(difference)
        minuend=int(max(list1))
        subtrahend=int(min(list1))
    if minuend == 1:
        print('COPRIME')
    else:
        print('NOT COPRIME')