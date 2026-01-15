#incorrect solution
'''
x = list(map(int,input().split()))
points = x[:2]
teleporter = x[2:]
dist = 0
if abs(points[0]-points[1]) <= abs(points[0]-teleporter[0]) and abs(points[0]-points[1]) <= abs(points[0]-teleporter[1]):
    dist += abs(points[0]-points[1])
elif abs(points[0]-teleporter[0]) <= abs(points[0]-teleporter[1]):
    dist += abs(points[0]-teleporter[0])
    dist += abs(teleporter[1]-points[1])
else:
    dist += abs(points[0]-teleporter[1])
    dist += abs(teleporter[0]-points[1])
print(dist)
'''

#claude's solution (correct)
x = list(map(int, input().split()))
a, b, x_tp, y_tp = x[0], x[1], x[2], x[3]

direct = abs(a - b)
via_x = abs(a - x_tp) + abs(y_tp - b)
via_y = abs(a - y_tp) + abs(x_tp - b)

print(min(direct, via_x, via_y))