a = int(input())
for b in range(a):
    sentence = list(input())
    for i,v in enumerate(sentence):
        if v.isalpha() == True or v == ' ' or v == '-':
            pass
        else:
            sentence.pop(i)
    if sentence[0].isalpha() == True:
        print(sentence[0].upper(),end='')
    for i,v in enumerate(sentence):
        if v == ' ' or v == '-':
            if i+1 < len(sentence):
                print(sentence[i+1].upper(),end='')
    print()