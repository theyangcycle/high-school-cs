#Tablulation
def fib(n):
    a,b = 0,1
    for i in range(n-1):
        a,b = b,a+b
    return a
print(fib(40))

#Memoization
seen = {1:0,2:1}
def fib(n):
    if n in seen:
        return seen[n]
    seen[n] = fib(n-1)+fib(n-2)
    return seen[n]
print(fib(40))