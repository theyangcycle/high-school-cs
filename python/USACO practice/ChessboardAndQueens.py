board = []
for _ in range(8):
    board.append(list(input()))

count = 0
def queens(coords,numq):
    global count
    global board
    if numq == 8:
        count += 1
        return
    for i in range(8):
        boo = True
        y = [j[1] for j in coords]
        if board[numq][i] == "*":
            continue
        if i in y:
            continue
        for j in coords:
            if abs((numq-j[0])/(i-j[1])) == 1:
                boo = False
                break
        if boo:
            coords.append([numq,i])
            numq += 1
            queens(coords[:],numq)
            coords.pop()
            numq -= 1

queens([],0)
print(count)