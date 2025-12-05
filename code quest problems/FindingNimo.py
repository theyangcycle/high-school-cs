a = int(input())
for b in range(a):
    x = input().split(' ')
    try:
        index = x.index('Nimo')
        print(index + 1)
    except ValueError:
        print('?')