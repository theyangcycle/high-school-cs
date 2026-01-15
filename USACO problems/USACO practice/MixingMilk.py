import sys
input = sys.stdin.readline
def print(_):
    sys.stdout.write(f'{_}\n')

cap1,amo1 = list(map(int,input().split()))
cap2,amo2 = list(map(int,input().split()))
cap3,amo3 = list(map(int,input().split()))

start = time.perf_counter()

for i in range(33):
    if amo1 + amo2 < cap2:
        amo2 += amo1
        amo1 = 0
    else:
        amo1 = amo1 + amo2 - cap2
        amo2 = cap2

    if amo2 + amo3 < cap3:
        amo3 += amo2
        amo2 = 0
    else:
        amo2 = amo2 + amo3 - cap3
        amo3 = cap3

    if amo3 + amo1 < cap1:
        amo1 += amo3
        amo3 = 0
    else:
        amo3 = amo3 + amo1 - cap1
        amo1 = cap1

if amo1 + amo2 < cap2:
        amo2 += amo1
        amo1 = 0
else:
    amo1 = amo1 + amo2 - cap2
    amo2 = cap2
    
print(amo1)
print(amo2)
print(amo3)