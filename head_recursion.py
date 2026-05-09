def head(n):
    if n == 0:
        return
    head(n-1)   # recursive call first
    print(n)    # work after
