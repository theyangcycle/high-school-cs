import copy

n = int(input())
capybaras = list(map(int,input().split()))
capybaras2 = copy.deepcopy(capybaras)
sort = sorted(capybaras,reverse=True)
count = 0
for i in range(n):
    if capybaras == sort:
        break
    nums = capybaras[i:]
    if max(nums) == nums[0]:
        continue
    else:
        id = nums.index(max(nums))+i
        move = capybaras[id]
        capybaras.pop(id)
        capybaras.insert(i,move)
        count+=1
count2 = 0
for i in range(n-1,-1,-1):
    if capybaras2 == sort:
        break
    nums = capybaras2[:i+1]
    if min(nums) == nums[-1]:
        continue
    else:
        id = nums.index(min(nums))
        move = capybaras2[id]
        capybaras2.pop(id)
        capybaras2.insert(i,move)
        count2 += 1
print(min(count,count2))