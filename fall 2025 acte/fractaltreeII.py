a = int(input())
for b in range(a):
    c = int(input())
    tree = []
    boo = True
    for d in range(c):
        tree.append(int(input()))
    for i in range(len(tree)-1):
        if tree[i+1] % tree[i] == 0:
            pass
        else:
            boo = False
            break
    if boo:
        print('YES')
    else:
        print('NO')