#Tablulation
def fib(n):
    dp = [0]*n
    dp[1] = 1
    for i in range(2,n):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[-1]
print(fib(40))

#Memoization
seen = {1:0,2:1}
def fib(n):
    if n in seen:
        return seen[n]
    seen[n] = fib(n-1)+fib(n-2)
    return seen[n]
print(fib(40))