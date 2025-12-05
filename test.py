import sys

input = sys.stdin.readline
print = sys.stdout.write

x = int(input())
while x != 1:
    print(f'{x} ')
    if x % 2 == 0:
        x //= 2
    else:
        x = x*3+1
    