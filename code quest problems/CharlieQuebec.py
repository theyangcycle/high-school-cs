alphabet_dict = {
    'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
    'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliet',
    'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
    'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray', 'Y': 'Yankee',
    'Z': 'Zulu', ' ':' ', '-': '-'
}

a=int(input())
for b in range(a):
    c=int(input())
    for d in range(c):
        x=input().upper()
        x=list(x)
        y = 0
        while x[len(x)-2] != '-':           
            if len(x) == 1:
                break
            if y == len(x)-1:
                break
            if x[y] == ' ':
                y+=1
                continue 
            if x[y] == '-':
                y+=1
                continue
            if x[y+1] == ' ':
                x[y]=alphabet_dict[x[y]]
                y+=1
            else:
                x[y]=alphabet_dict[x[y]]
                x.insert(y+1,'-')
                y+=1
        x[len(x)-1]=alphabet_dict[x[len(x)-1]]
        x=''.join(x)
        print(x)