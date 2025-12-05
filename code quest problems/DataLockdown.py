a = int(input())
for b in range(a):
    c = int(input())
    x = []
    for d in range(c):
        website = input().split(' ')
        if '.lmco.com' in website[0]:
            continue
        elif int(website[1]) < 1000:
            continue
        else:
            x.append(' '.join(website))
    print('\n'.join(x))