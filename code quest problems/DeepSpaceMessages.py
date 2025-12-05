number_to_letter = {}

for i in range(1, 27):
    number_str = str(i)
    letter = chr(i + 96)
    number_to_letter[number_str] = letter

def map_numbers(num):
    global number_to_letter
    let = number_to_letter[num]
    return let

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

a = int(input())
for b in range(a):
    dataStream = input()
    result = []
    i = 0

    while i != len(dataStream):
        x = is_number(dataStream[i])
        if x == False:
            i+=1
            continue
        else:   
            y1 = is_number(dataStream[i])
            if i == len(dataStream) - 1:
                if y1 == True:
                    result.append(dataStream[i])
                    i+=1
                    continue
                else:
                    continue
            y2 = is_number(dataStream[i+1])
            if y2 == True:
                result.append(str(dataStream[i])+str(dataStream[i+1]))
                i+=2
            else:
                result.append(dataStream[i])
                i+=1

    result = ''.join(list(map(map_numbers,result)))
    print(result)