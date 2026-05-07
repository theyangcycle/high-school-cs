from collections import defaultdict
dd = defaultdict(int)

x = input().lower()
words = []
for i in range(len(x)):
    if x[i].isalpha() == True:
        words.append(x[i])
for j in words:
    dd[j]+=1
s = []
for n in words:
    if n not in s:
        s.append(n)


for k in s:
    print(f'{k}: {dd[k]}',end=' ')