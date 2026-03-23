x = list(input())
for i in range(len(x)):
    if x[i] == '|':
        x[i] = ' '
print(''.join(x))