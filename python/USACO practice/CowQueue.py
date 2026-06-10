queue = []
with open("cowqueue.in", "r") as file:
    n = file.readline()
    for line in file:
        queue.append(list(map(int,line.split())))
queue.sort()
time = queue[0][0] + queue[0][1]
for i in range(1,len(queue)):
    if queue[i][0] >= time:
        time = queue[i][0] + queue[i][1]
    else:
        time += queue[i][1]
with open("cowqueue.out", "w") as file:
    file.write(str(time))