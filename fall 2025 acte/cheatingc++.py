a = int(input())
cpp = []
for b in range(a):
    c = input()
    cpp.append(c)
for i in range(len(cpp)):
    if 'for' in cpp[i][:3] or 'while' in cpp[i][:5] or 'if' in cpp[i][:2]:
        pass
    else:
        if cpp[i][-1] == ';':
            pass
        else:
            cpp[i] = cpp[i] + ';'
print('\n'.join(cpp))