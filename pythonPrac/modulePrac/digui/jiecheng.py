def calc(n):
    if n==1:
        return 1
    else:
        return n * calc(n-1)
    
    
print(calc(5))