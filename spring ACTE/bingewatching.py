start = list(map(int,input().split(':')))
last = list(map(int,input().split(':')))
output = []
start = start[0]*3600+start[1]*60+start[2]
last = last[0]*3600+last[1]*60+last[2]
time = last-start
minsec = time%3600
output.append((time-minsec)//3600)
sec = minsec % 60
output.append((minsec-sec)//60)
output.append(sec)
for i in range(len(output)):
    output[i] = str(output[i]).rjust(2,'0')
print(':'.join(output))