x=int(input())
for z in range(1, x+1):
  y=input().split(' ')
  num = 0
  a = int(y[0])
  b = int(y[1])
  c = int(y[2])
  while num != c:
    if num == 0:
      num = num + b * 5
    if num < c:
      num+=a
      if num < c:
        break
      if num > c:
        while num > c:
          num-=1
    if num > c:
      while num > c:
        num-=5
      if num == 0:
        num+=a
        if num < c:
          break
        if num > c:
          while num > c:
            num-=1
  if num !=c:
    print('false')
    continue
  print('true')