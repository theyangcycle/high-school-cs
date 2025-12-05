x=int(input())
for z in range(1, x+1):
  y=input()
  a = list(y)
  if a[9] == 'X':
    a[9] = '10'
  a = list(map(int, a))
  S = (a[0] * 10) + (a[1] * 9) + (a[2] * 8) +     (a[3] * 7) + (a[4] * 6) + (a[5] * 5) + (a[6]    * 4) + (a[7] * 3) + (a[8] * 2)
  b = (S + a[9]) % 11
  if b == 0:
    print('VALID')
  else:
    print('INVALID')