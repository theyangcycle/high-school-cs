a = int(input())
for b in range(a):
    num = int(input())
    string = input().split()
    new = ""
    for i in range(num):
        temp = []
        temp.extend([new+string[i],string[i]+new])
        temp = sorted(temp)
        new = temp[0]
    print(new)