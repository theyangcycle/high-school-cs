elements = ['Wood', 'Fire', 'Earth', 'Metal', 'Water']
animals = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 
           'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']

a=int(input())
for b in range(a):
    answer = []
    year = int(input())
    if year % 2 == 0:
        answer.append('Yang')
    else:
        answer.append('Yin')
    
    element_num = int((((year-4) % 10)/2)//1)
    answer.append(elements[element_num])
    
    animal_num = (year-4)%12
    answer.append(animals[animal_num])
    answer = ' '.join(answer)
    print(str(year) + ' ' + answer)