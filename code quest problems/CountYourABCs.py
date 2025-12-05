a = int(input())
for b in range(a):
    
    def remove_character_from_list(input_list, char_to_remove):
        for i in reversed(range(len(input_list))):
            if input_list[i] == char_to_remove:
                del input_list[i]
        return input_list
    
    x = list(input())
    remove_character_from_list(x,' ')
    y = []
    for z in range(len(x)):
        y.append(x.count(x[z]))
    print(max(y))