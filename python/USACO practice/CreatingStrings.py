'''letters = input()
seen = set()
def perm(new,left):
    if len(left) == 0:
        seen.add(new)
        return
    for i in range(len(left)):
        new += left[i]
        x = left.pop(i)
        perm(str(new),left[:])
        new = new[:-1]
        left.insert(i,x)
perm("",list(letters))
print(len(seen))
print('\n'.join(sorted(seen)))'''

letters = input()
seen = {""}
for _ in letters:
    newseen = set()
    for i in seen:
        for j in range(len(i)+1):
            newseen.add(i[:j]+_+i[j:])
    seen = newseen
print(len(seen))
print('\n'.join(sorted(seen)))