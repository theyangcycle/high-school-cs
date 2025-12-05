a=int(input())
for b in range(a):
    x=str(input())
    if 'red' in x:
        print('red')
    elif 'blue' in x:
        print('blue')
    else:
        print('no color found')