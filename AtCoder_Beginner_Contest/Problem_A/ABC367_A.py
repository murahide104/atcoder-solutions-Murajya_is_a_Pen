a, b, c = map(int, input().split())

if c < b:
    if a < b and c < a:
        print('Yes')
    else:
        print('No')
else:
    if a < b or c < a:
        print('Yes')
    else:
        print('No')