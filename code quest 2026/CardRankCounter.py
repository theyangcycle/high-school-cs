from collections import defaultdict
t = int(input())
for _ in range(t):
    a = int(input())
    cards = []
    count = defaultdict(int)
    for b in range(a):
        card = input()
        cards.append(card)
    check = input()
    for i in cards:
        count[i] += 1
    print(count[check])