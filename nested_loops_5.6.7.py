n = int(input())
x = 64

while n >= 1:
    if n >= x:
        n -= x
    else:
        x /= 2

    
    print(f'{int(x)}', end = ' ')