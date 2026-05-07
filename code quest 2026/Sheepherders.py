a = int(input())
for b in range(a):
    miles,time = input().split()
    time = list(map(int,time.split(':')))
    time = time[0]*60+time[1]
    miles = float(miles)
    miles -= 1
    count = 0
    for i in range(int(miles)*70):
        miles -= 300/(time-60)
        miles -= 300/(time+60)
        if miles >= 1:
            count +=1
        else:
            break
    print(count)