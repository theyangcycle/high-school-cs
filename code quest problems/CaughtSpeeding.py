x=int(input())
for z in range(1, x+1):
  y=input().split(' ')
  a = int(y[0])
  if y[1] == 'false':
    if a <= 60:
      print('no ticket')
    elif a >= 61 and a <= 80:
      print('small ticket')
    elif a >= 81:
      print('big ticket')
  if y[1] == 'true':
    if a <= 65:
      print('no ticket')
    elif a >= 66 and a <= 85:
      print('small ticket')
    elif a >= 86:
      print('big ticket')