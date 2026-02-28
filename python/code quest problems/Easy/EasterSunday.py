t = int(input())
for _ in range(t):
    y = int(input())
    a = y%19
    b = y%4
    c = y%7
    k = y//100
    p = (13+8*k)//25
    q = k//4
    m = (15-p+k-q)%30
    n = (4+k-q)%7
    d = (19*a+m)%30
    e = (2*b+4*c+6*d+n)%7
    f = (11*m+11)%30
    day = int(22+d+e)
    if day <= 31:
        print(f'{y}/03/{str(day).rjust(2,'0')}')
    else:
        day-=31
        if d == 28 and e == 6 and f<19:
            day = 18
            print(f'{y}/04/{day}')
        elif d == 29 and e == 6:
            day = 19
            print(f'{y}/04/{day}')
        else:
            print(f'{y}/04/{str(day).rjust(2,'0')}')