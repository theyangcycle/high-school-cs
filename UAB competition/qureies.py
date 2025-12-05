n = int(input())
nline = list(map(int,input().split()))
m = int(input())
for o in range(m):
    m1,m2 = map(int,input().split())
    newline = []
    for i in range(m1,m2+1):
        newline.append(nline[i])
    print(f'{min(newline)} {max(newline)}')