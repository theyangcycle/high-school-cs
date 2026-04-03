n = int(input())
bites = 0
while n > 0:
    if n % 2 == 1:
        bites += 1
        n -= 1
    else:
        n = list(map(int,list(str(n))))
        n = [num for num in n if num % 2 != 0]
        n = ''.join(list(map(str,n)))
        n = int(n)
        bites+=1
print(bites%(10**9+7))