x = input().split()
output = []
while len(x) != 0:
    count = 0
    y = x[0]
    i = 0
    while i < len(x):
        if y == x[i]:
            count += 1
            x.pop(i)
        else:
            i += 1
    for j in range(6-count):
        output.append(y)
print(' '.join(sorted(output)))