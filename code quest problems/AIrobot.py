a=int(input())
for b in range(a):
    x=str(input())
    y=x.split(" ")
    y1=y[:3]
    y2=y[3:]
    y2=str(y2[0])
    for z in range(len(y2)):
        if str(y2[z]) == "R":
            if y1[2] == "N":
                y1[2] = "E"
                continue
            if y1[2] == "E":
                y1[2] = "S"
                continue
            if y1[2] == "W":
                y1[2] = "N"
                continue
            if y1[2] == "S":
                y1[2] = "W"
                continue
        if str(y2[z]) == "L":
            if y1[2] == "N":
                y1[2] = "W"
                continue
            if y1[2] == "E":
                y1[2] = "N"
                continue
            if y1[2] == "W":
                y1[2] = "S"
                continue
            if y1[2] == "S":
                y1[2] = "E"
                continue
        if str(y2[z]) == "A":
            if y1[2] == "N":
                y1[1] = int(y1[1]) + 1
                continue
            if y1[2] == "E":
                y1[0] = int(y1[0]) + 1
                continue
            if y1[2] == "W":
                y1[0] = int(y1[0]) - 1
                continue
            if y1[2] == "S":
                y1[1] = int(y1[1]) - 1
                continue
    print(str(y1[0])+" "+str(y1[1])+" "+str(y1[2]))