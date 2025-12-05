x=int(input())
for i in range(1, x+1):
  y=input().split('|')
  a=y[0]
  b=y[1]
  f=list(a)
  g=list(b)
  d=0
  if a == b:
    print(a + "|" + b + ' = ' + 'NOT AN ANAGRAM')
    continue
  if ' ' in a or ' ' in b:
    print(a + "|" + b + ' = ' + 'NOT AN ANAGRAM')
    continue
  c=len(f)
  e=len(g)
  if c!=e:
    print(a + "|" + b + ' = ' + 'NOT AN ANAGRAM')
    continue
  while d<=c:
    if d == c:
      print(a + "|" + b + ' = ' + 'ANAGRAM')
      break
    elif f[0] in g and g[0] in f:
      d+=1
      g.remove(f[0])
      f.pop(0)
    else:
      print(a + "|" + b + ' = ' + 'NOT AN ANAGRAM')
      break