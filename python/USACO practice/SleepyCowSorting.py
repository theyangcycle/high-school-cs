with open("sleepy.in") as f:
    n = int(f.readline())
    order = list(map(int,f.readline().split()))

least = min(order)
greatest = max(order)
sort = sorted(order)
count = 0

while order != sort:
    if order[0] == greatest:
        temp = order.pop(0)
        order.append(temp)
    elif order[0]+1 == order[1]:
        if order[0] == least:
            i = order.index(greatest)
            temp = order.pop(0)
            order.insert(i,temp)
        else:
            i = order.index(order[0]-1)
            temp = order.pop(0)
            order.insert(i,temp)
    else:
        i = order.index(order[0]+1)
        temp = order.pop(0)
        order.insert(i-1,temp)
    
    count += 1

with open("sleepy.out", "w") as f:
    f.write(str(count))