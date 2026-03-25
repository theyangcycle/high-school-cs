abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def decode(abc,ABC):
    string = input("Enter text you want to decode: ")
    print()
    print(f'Shifted 0: {string}')
    print()
    for b in range(1,27):
        output = []
        for i in string:
            if i.isalpha() == False:
                output.append(i)
                continue
            elif i in abc:
                x = abc.index(i) - b
                if x < 0:
                    output.append(abc[26+x])
                else:
                    output.append(abc[x])
            else:
                x = ABC.index(i) - b
                if x < 0:
                    output.append(ABC[26+x])
                else:
                    output.append(ABC[x])
        print(f'Shifted {b}: {''.join(output)}')
        print()

def encode(abc,ABC):
    string = input("Enter text you want to encode: ")
    shift = int(input("Enter a positive integer for the shift: "))
    print()
    output = []
    for i in string:
        if i.isalpha() == False:
            output.append(i)
            continue
        elif i in abc:
            x = abc.index(i) + shift
            if x > 25:
                output.append(abc[x-26])
            else:
                output.append(abc[x])
        else:
            x = ABC.index(i) + shift
            if x > 25:
                output.append(ABC[x-26])
            else:
                output.append(ABC[x])
    print(''.join(output))
    print()

while True:
    choice = input("Enter 1 to encode text, 2 to decode text, or anything else to quit: ")
    if choice == '1':
        encode(abc,ABC)
    elif choice == '2':
        decode(abc,ABC)
    else:
        break