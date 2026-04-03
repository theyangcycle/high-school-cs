n = int(input())
weights = list(map(int,input().split()))
useful = list(map(int,input().split()))
limit = int(input())
max_use = 0
backpack = []
for i in range(n):
    id = useful.index(max(useful))
    if sum(backpack)+weights[id] > limit:
        useful.pop(id)
        weights.pop(id)
    else:
        backpack.append(weights[id])
        max_use += useful[id]
        useful.pop(id)
        weights.pop(id)
print(max_use)