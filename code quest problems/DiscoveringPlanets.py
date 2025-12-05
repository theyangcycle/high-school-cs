a = int(input())
for b in range (a):
        x = input().split(' ')
        if float(x[0]) > 100:
            print('The planet is too hot.')
        elif float(x[0]) < 0:
            print('The planet is too cold.')
        elif x[1] == 'false':
            print('The planet has no water.')
        elif x[2] == 'false':
            print('The planet has no magnetic field.')
        elif float(x[3]) > 0.6:
            print('The planet\'s orbit is not ideal.')
        else:
            print('The planet is habitable')             