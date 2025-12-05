a=int(input())
for b in range(a):
    x = input()
    x = x.split(',')
    V=(float(x[0])*float(x[1]) + float(x[2])*float(x[3])) / (float(x[1])+float(x[3]))
    rounded_V = f"{V:.2f}"
    print(rounded_V)