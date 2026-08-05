t, k = map(int,input().split())
for i in range(t):
    n = int(input())
    s = list(input())
    print("YES")
    ans = ''
    flipped = 1
    if k == 1:
        for i in range(len(s) - 1, -1, -1):
            char = s.pop(i)
            if flipped % 2 == 0:
                if char == 'M':
                    char = 'O'
                else:
                    char = 'M'
            if char == 'O':
                flipped += 1
            ans = char + ans
        print(ans)