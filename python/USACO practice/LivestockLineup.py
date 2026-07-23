from collections import defaultdict

COWS = sorted(
	["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"]
)
rules = []
with open("lineup.in") as f:
    n = int(f.readline())
    for i in range(n):
        x = f.readline().split()
        rules.append([x[0],x[-1]])

count = defaultdict(int)

for i in rules:
    for j in i:
        count[j] += 1

order = []
for i in COWS:
    if i not in order and count[i] <= 1:
        order.append(i)
        for j in rules:
            if i in j:
                if j[0] == i:
                    if j[1] not in order:
                        order.append(j[1])
                else:
                    if j[0] not in order:
                        order.append(j[0])

with open("lineup.out","w") as f:
    f.write('\n'.join(order))