def anagram(word1,word2):
    if len(word1) == len(word2):
        word1,word2 = list(word1.lower()),list(word2.lower())
        for i in word1:
            if i in word2:
                word2.pop(word2.index(i))
            else:
                return False
        return True
    else:
        return False

a = int(input())
for b in range(a):
    inp = input()
    positions = inp[:inp.index(' ')]
    idx1 = inp.index('\"')+1
    idx = inp.index('\"',idx1)+1
    sent1 = inp[idx1:idx-1].split()
    sent2 = inp[idx+2:-1].split()
    positions = [positions[positions.index('[')+1:positions.index(',')],positions[positions.index(',')+1:positions.index(']')]]
    boo = anagram(sent1[int(positions[0])-1],sent2[int(positions[1])-1])
    if boo:
        print("Verified")
    else:
        print("Intercepted")