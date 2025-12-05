def hamming(fword, lword):
  u=len(lword)
  v=len(fword)
  w=0
  ham = 0
  while w<u:
    if u != v:
      ham = 999999
      break
    if fword[w] != lword[w]:
      ham+=1
      w+=1
    else:
      w+=1
  return ham

x=int(input())
for i in range(1, x+1):
  y=input().split(' ')
  a = int(y[0])
  b = int(y[1])
  c = []
  for j in range(1, a+b+1):
    z=input()
    c.append(z)
    d = len(c)
    if d == a+b:
      e = slice(a)
      f = slice(a, d)
      g = c[e]
      h = c[f]
      k=0
      l=0
      d=[]
      while k < b:
        m = hamming(g[l], h[k])
        d.append(m)
        l+=1
        if len(d) == a:
          n=min(d)
          o=d.index(n)
          print(g[o])
          l=0
          k+=1
          d=[]