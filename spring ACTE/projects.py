n = int(input())
projects = []
money = []
for b in range(n):
    x = list(map(int,input().split()))
    projects.append(x)
for i in range(n):
    m = 0
    m += projects[i][2]
    ids = []
    for j in range(n):
        if projects[j] == projects[i]:
            continue
        if projects[i][1]<projects[j][0]:
            ids.append(projects[j][2])
    if ids != []:
        m+=max(ids)
    money.append(m)
print(max(money))