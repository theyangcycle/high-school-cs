from decimal import Decimal,ROUND_HALF_UP

def invert(list1):
    global determinant
    x = Decimal(list1*determinant)
    x = x.quantize(Decimal('0.001'), rounding = ROUND_HALF_UP)
    return x

matrix = input('Enter a 2x2 matrix: ').split(' ')
matrix = list(map(Decimal,matrix))
determinant = 1/(matrix[0]*matrix[3] - matrix[1]*matrix[2])
matrix[1],matrix[2] = -matrix[1],-matrix[2]
matrix[0],matrix[3] = matrix[3],matrix[0]

matrix = list(map(invert,matrix))
matrix = ' '.join(list(map(str,matrix)))
print(matrix)