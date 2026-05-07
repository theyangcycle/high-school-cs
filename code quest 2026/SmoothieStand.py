a = int(input())
strawberrySwirl = ['strawberry','blueberry']
bananaBurst = ['banana','kiwi','orange']
tropicalTango = ['kiwi','orange','mango','blueberry']
mangoMedley = ['mango','strawberry','blueberry','banana']
for b in range(a):
    ingredients = input().split('|')
    smoothie = input()
    boo = True
    if smoothie == 'strawberry swirl':
        for i in strawberrySwirl:
            if i not in ingredients:
                boo = False
    elif smoothie == 'banana burst':
        for i in bananaBurst:
            if i not in ingredients:
                boo = False
    elif smoothie == 'tropical tango':
        for i in tropicalTango:
            if i not in ingredients:
                boo = False
    else:
        for i in mangoMedley:
            if i not in ingredients:
                boo = False
    if boo:
        print("YES")
    else:
        print("NO")