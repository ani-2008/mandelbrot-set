MAX_ITER = 100

def mandel(c):
    z = 0
    n = 0

    while abs(z) <= 2 and n < MAX_ITER:
        z = z * z + c
        n += 1
    return n


