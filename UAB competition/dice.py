a = int(input())
for b in range(a):
    n,d,t = map(int,input().split())
    count = 0
    if n == 1:
        count = 1
    else:
        dice = []
        for i in range(n,d+1):
            for j in range(1,d+1):
                dice.append(j+i)
        for i in range(len(dice)):
            if dice[i] == t:
                count+=1
    
    print(count)