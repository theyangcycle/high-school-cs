a = int(input())
for b in range(a):
    cylinders,gas,maxGas,num = map(float,input().split())
    segments = []
    for i in range(int(num)):
        segment = input().split()
        segment[1] = float(segment[1])
        segments.append(segment)
    for i in segments:
        if gas > 0:
            if i[0] == 'C':
                if cylinders == 4:
                    base = 28
                elif cylinders == 6:
                    base = 22
                else:
                    base = 18
            elif i[0] == 'H':
                if cylinders == 4:
                    base = 35
                elif cylinders == 6:
                    base = 28
                else:
                    base = 22
            else:
                if cylinders == 4:
                    base = 20
                elif cylinders == 6:
                    base = 15
                else:
                    base = 12
            effective = base - (0.25*(maxGas-gas))
            gas -= i[1]/effective
    if gas <= 0:
        print("NO")
    else:
        print("YES")