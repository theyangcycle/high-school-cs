import sys

x,y = list(map(int,sys.stdin.readline().split()))
for i in range(y):
    if x % 2 == 1:
        x = x*3+1
    else:
        x //=2
sys.stdout.write(str(x))