def calc(n):
    if n==1:
        return 1
    else:
        return n * calc(n-1)
    
    # hhh
    
print(calc(5))