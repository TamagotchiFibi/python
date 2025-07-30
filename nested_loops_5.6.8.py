n = int(input())
x = 64

while n >= 1:
    if n >= x:
        n -= x
        print(f'{int(x)}', end = ' ')
    else:
        x /= 2