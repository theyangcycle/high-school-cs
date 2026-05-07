a = list(input().lower())
b = list(input().lower())
x = []
y = []
for i in range(len(a)):
    if a[i].isalpha() == True:
        x.append(a[i])
for j in range(len(b)):
    if b[j].isalpha() == True:
        y.append(b[j])

if x == y:
    print('false')
elif sorted(x) == sorted(y):
    print('true')
else:
    print('false')