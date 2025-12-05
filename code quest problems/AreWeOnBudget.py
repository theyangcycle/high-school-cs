from decimal import Decimal, ROUND_HALF_UP

a = int(input())
for b in range(a):
    num = int(input())
    budget = list(map(Decimal,input().split(' ')))
    real = list(map(Decimal,input().split(' ')))
    average_list = []
    for i in range(num):
        average_list.append(real[i]-budget[i])
    average = Decimal(sum(average_list)/len(average_list))
    average = average.quantize(Decimal('0.01'), rounding = ROUND_HALF_UP)
    print(average)