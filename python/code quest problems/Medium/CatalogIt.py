from collections import defaultdict
a = int(input())
roots = []
children = defaultdict(list)
for b in range(a):
    name,parent = input().split(',')
    if parent == 'None':
        roots.append(name)
    else:
        children[parent].append(name)
def x(name,depth):
    print('-'*depth + name)
    for i in sorted(children[name]):
        x(i,depth+1)
for j in sorted(roots):
    x(j,0)