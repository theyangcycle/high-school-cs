words = input()
word = input()
for i in range(len(words)):
    try:
        if words[i].isalpha() == True or words[i] == ' ':
            pass
        else:
            words = words[:i]+words[i+1:]
    except:
        break
words = words.split()
count = 0
for i in words:
    if i.lower() == word:
        count+=1
print(count)