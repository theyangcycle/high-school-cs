
n,k = map(int,input().split())
essay = input().split()
line = []
space = 0
for i in range(n):
    if len(line)-space < k:
        if len(line) + len(essay[i]) - space > k:
            line.pop(0)
            print(''.join(line))
            line = []
            space = 0  
            line.append(' ')
            space += 1
            line.extend(essay[i])
        else:
            line.append(' ')
            space += 1
            line.extend(essay[i])
    else:
        line.pop(0)
        print(''.join(line))
        line = []
        space = 0  
        line.append(' ')
        space += 1
        line.extend(essay[i])

line.pop(0)
print(''.join(line))
'''
n, k = map(int, input().split())
words = input().split()

current_line = ""
current_len = 0

for word in words:
    if current_len + len(word) <= k:
        if current_line:
            current_line += " "
        current_line += word
        current_len += len(word)
    else:
        print(current_line)
        current_line = word
        current_len = len(word)

print(current_line)
'''