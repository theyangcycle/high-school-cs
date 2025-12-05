a = int(input())
for b in range(a):
    readingnull = input().split(' ')
    readingthird = input().split(' ')
    readingnull = list(map(float,readingnull))
    readingthird = list(map(float,readingthird))
    multinum = 0
    multiindex = []
    for i in range(len(readingnull)):
        if 0.6 <= readingnull[i] <= 0.85:
            if 0.6 <= readingthird[i] <= 0.85:
                multinum += 1
                multiindex.append(str(i))
    multiindex = ' '.join(multiindex)
    if multinum == 0:
        print('No multipaction events detected.')
    elif multinum == 1:
        print(f'A multipaction event was detected at time index {multiindex}.')
    else:
        print(f'{multinum} multipaction events were detected at time indices: {multiindex}.')