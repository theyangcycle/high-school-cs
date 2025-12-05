s = input()
s = s.split(':')
if s[2][2] == 'A':
    if s[0] == '12':
        s[0] = int(s[0])
        s[0] = '00'
elif s[2][2] == 'P':
    if s[0] != '12':
        s[0] = int(s[0])
        s[0] = str(s[0]+12)
s[2] = s[2][0] + s[2][1]
print(':'.join(s))
