num,wem = list(map(int,input().split()))
players = sorted(list(map(int,input().split())))
select = 0
for i in range(len(players)-1,-1,-1):
    avg = round(sum(players)/len(players),2)
    if wem >= avg:
        select += 1
print(select)