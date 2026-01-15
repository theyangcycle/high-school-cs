a = int(input())
one = 0
two = 0
three = 0

def one1(x):
    global one
    global a
    location = 1
    for i in range(a):
        if x[i][0] == location:
            location = x[i][1]
        elif x[i][1] == location:
            location = x[i][0]
        if x[i][2] == location:
            one += 1

def two2(x):
    global two
    global a
    location = 2
    for i in range(a):
        if x[i][0] == location:
            location = x[i][1]
        elif x[i][1] == location:
            location = x[i][0]
        if x[i][2] == location:
            two += 1

def three3(x):
    global three
    global a
    location = 3
    for i in range(a):
        if x[i][0] == location:
            location = x[i][1]
        elif x[i][1] == location:
            location = x[i][0]
        if x[i][2] == location:
            three += 1


x = []
for b in range(a):
    x.append(list(map(int,input().split())))
one1(x)
two2(x)
three3(x)
print(max(one,two,three))