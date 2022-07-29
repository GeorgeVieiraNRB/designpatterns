def fib(x):
    if x==0 or x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)
def verify(z):
    flag=False
    cont=0
    k=0
    while k<z:
        k=fib(cont)
        print(k)
        if k==z:
            flag=True
            break
        cont=cont+1
    return flag
print(verify(34))
print(verify(35))
