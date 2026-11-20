def storsta_talet(a, b, c):
    if a > b:
        if a > c:
            storsta = a
        else:
            storsta = c
    else:
        if c > b:
            storsta = c
        else:
            storsta = b
    return storsta
