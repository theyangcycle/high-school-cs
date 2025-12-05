x=int(input())
for z in range(1, x+1):
  y=input().split(':')
  a=y[0]
  b=y[1].split(',')
  c=len(b)
  e=0
  one=0
  two=0
  three=0
  HR=0
  total=0
  while e<c:
    if b[e] == 'BB':
      e+=1
      continue
    elif b[e] == 'K':
      e+=1
      total+=1
    elif b[e] == '1B':
      e+=1
      one+=1
      total+=1
    elif b[e] == '2B':
      e+=1
      two+=1
      total+=1
    elif b[e] == '3B':
      e+=1
      three+=1
      total+=1
    elif b[e] == 'HR':
      e+=1
      HR+=1
      total+=1
  if total==0:
    print(a+'='+'0.000')
    continue
  SLG = (one+(2*two)+(3*three)+(4*HR))/total
  d=round(SLG,3)
  fillchar='0'
  f=str(d).ljust(5, fillchar)
  print(a+'='+str(f))