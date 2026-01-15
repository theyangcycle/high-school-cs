n,k = list(map(int,input().split()))
q = int(input())
myList = []
for _ in range(q):
    myList.append(list(map(int,input().split())))
x = myList[0][0]
y = myList[0][1]
mai = myList[0][2]
print(mai)
for i in range(1,len(myList)):
    r = myList[i][0]
    c = myList[i][1]
    v = myList[i][2]
    if r == x and c == y:
        mai = v
    elif abs(r - x) < k and abs(c - y) < k:
        mai += v
        x = r
        y = c
    print(mai)