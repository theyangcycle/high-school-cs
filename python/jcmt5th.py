key = ['c','a','b','b','d','d','d','d','e','c','a','a','c','b','b']
answers = input().split()
if len(answers) == 15:
    score = 0
    for i in range(len(key)):
        if answers[i] == 'x':
            continue
        elif answers[i] == key[i]:
            score += 4
        else:
            score -= 1
    print(score)