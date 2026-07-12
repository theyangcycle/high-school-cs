output = ''
cows = {
    "Bessie":0,
    "Elsie":0,
    "Daisy":0,
    "Gertie":0,
    "Annabelle":0,
    "Maggie":0,
    "Henrietta":0,
}
with open("notlast.in") as f:
    n = int(f.readline())
    for i in range(n):
        cow = f.readline().split()
        cows[cow[0]] += int(cow[1])

sorted_cows = dict(sorted(cows.items(), key=lambda item: item[1]))
key = list(sorted_cows.keys())
vals = list(sorted_cows.values())
if len(set(vals)) == 1:
    output = 'Tie'
else:
    for i in range(len(key)):
        if vals[i] > vals[0]:
            try:
                if vals[i+1] == vals[i]:
                    output = 'Tie'
                else:
                    output = str(key[i])
            except:
                output = str(key[i])
            break
with open("notlast.out", "w") as f:
    f.write(output)