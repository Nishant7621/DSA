def print_tail(n):
    if n==0:
        return
    print(n)
    print_tail(n-1)

print(print_tail(5))