a = int(input())
for b in range(a):
    num,unit1,unit2 = input().split()
    num = int(num)
    num1 = num
    if unit1 == "MINUTES":
        num1 *= 60
    elif unit1 == "HOURS":
        num1 *= 3600
    elif unit1 == "DAYS":
        num1 *= 86400
    if unit2 == 'SECONDS':
        print(f'{num} {unit1}->{num1} {unit2}')
    elif unit2 == 'MINUTES':
        print(f'{num} {unit1}->{int(num1/60)} {unit2}')
    elif unit2 == "HOURS":
        print(f'{num} {unit1}->{int(num1/3600)} {unit2}')
    else:
        print(f'{num} {unit1}->{int(num1/86400)} {unit2}')