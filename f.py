def fact(n,x):
    f1=1
    fact=1
    for i in range(1,n+1):
        f1=f1*x
        fact=fact*i
    return f1,fact
