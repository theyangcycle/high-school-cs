a = int(input())
for b in range(a):
    string = input()
    string = list(string[1:-1])
    the = set(string)
    if the == {' '}:
        print("No Letter Found")
    else:
        for i in range(len(string)-1,-1,-1):
            if string[i].isalpha() == True:
                print(string[i])
                break