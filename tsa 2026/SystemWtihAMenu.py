order = input()
if order == "[]":
    print('Total is: $0.00')
else:
    order = order[2:-2]
    order = order.split('\", \"')
    total = 0.0
    for i in order:
        if i == "Coffee":
            total += 3.50
        elif i == "Muffin":
            total += 2.75
        elif i == "Tea":
            total += 2.25
        elif i == "Scone":
            total += 3.00
    total = str(total).split('.')
    total[1] = total[1].ljust(2,"0")
    print(f'Total is: ${'.'.join(total)}')