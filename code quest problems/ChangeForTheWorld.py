x=int(input())
for z in range(x):
  y=input()
  w=y
  y = y.replace('$', '')
  y = y.replace('.', '')
  y = int(y)
  a = 0
  Q = 0
  D = 0
  N = 0
  P = 0
  print(w)
  while a < y:
    a+=25
    Q+=1
  if a==y:
    print('Quarters='+str(Q))
    print('Dimes='+str(0))
    print('Nickels='+str(0))      
    print('Pennies='+str(0))
  else:
    Q-=1
    a-=25
    print('Quarters='+str(Q))
    while a < y:
      a+=10
      D+=1
    if a==y:
      print('Dimes='+str(D))
      print('Nickels='+str(0))      
      print('Pennies='+str(0))
    else:
      D-=1
      a-=10
      print('Dimes='+str(D))
      while a < y:
        a+=5
        N+=1
      if a==y:
        print('Nickels='+str(N))      
        print('Pennies='+str(0))
      else:
        N-=1
        a-=5
        print('Nickels='+str(N))
        while a < y:
          a+=1
          P+=1
        print('Pennies='+str(P))