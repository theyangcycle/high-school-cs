x = list(input())
x.pop(-2)
x.pop(-1)
x = ''.join(x)
x = int(x)
if x % 100 in [11,12,13]:
    print(f'{x}th')
else:
    if x % 10 == 1:
        print(f'{x}st')
    elif x % 10 == 2:
        print(f'{x}nd')
    elif x % 10 == 3:
        print(f'{x}rd')
    else:
        print(f'{x}th')