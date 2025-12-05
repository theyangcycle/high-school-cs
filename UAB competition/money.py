import sys
input = sys.stdin.readline
def print(text):
    sys.stdout.write(f'{text}\n')
a = int(input())
for b in range(a):
    m = list(map(float,input().split()))
    change = m[1] - m[0]
    output = [0,0,0,0,0,0,0]
    while change >= 20:
        change = round(change - 20,2)
        output[0] += 1
    while change >= 10:
        change = round(change - 10,2)
        output[1] += 1
    while change >= 5:
        change = round(change - 5,2)
        output[2] += 1
    while change >= 1:
        change = round(change - 1,2)
        output[3] += 1
    while change >= 0.25:
        change = round(change - 0.25,2)
        output[4] += 1
    while change >= 0.1:
        change = round(change - 0.10,2)
        output[5] += 1
    while change >= 0.05:
        change = round(change - 0.05,2)
        output[6] += 1
    print(' '.join(list(map(str,output))))