buckets = [list(input()),list(input()),list(input()),list(input()),list(input()),list(input()),list(input()),list(input()),list(input()),list(input())]
barn = []
lake = []
for i in range(len(buckets)):
    if 'B' in buckets[i]:
        barn.append(i)
        barn.append(buckets[i].index('B'))
    elif 'L' in buckets[i]:
        lake.append(i)
        lake.append(buckets[i].index('L'))
print(abs(barn[0]-lake[0])+abs(barn[1]-lake[1])-1)
