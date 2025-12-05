color = {
    'red-violet':['blue','red'],'violet':['blue','red'],'blue-violet':['blue','red'],
    'blue-green':['blue','yellow'],'green':['blue','yellow'],'yellow-green':['blue','yellow'],
    'yellow-orange':['red','yellow'],'orange':['red','yellow'],'red-orange':['red','yellow']
}
a=int(input())
for b in range(a):
    x=str(input())
    if x == 'red':
        print('No colors need to be mixed to make '+x+'.')
        continue
    if x == 'blue':
        print('No colors need to be mixed to make '+x+'.')
        continue
    if x == 'yellow':
        print('No colors need to be mixed to make '+x+'.')
        continue
    else:
        x1 = color[x]
        print('In order to make ' + x + ', ' + x1[0] + ' and ' + x1[1] + ' must be mixed.')