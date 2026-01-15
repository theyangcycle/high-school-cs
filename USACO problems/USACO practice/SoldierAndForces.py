nums = list(map(int,input().split(' ')))
total = 0
for i in range(1,nums[2]+1):
    total += nums[0]*i
if total - nums[1] <= 0:
    print(0)
else:
    print(total - nums[1])