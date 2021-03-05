def fib(nthNum):
    j =0 
    k=0 
    fib = 0

    for i in range(nthNum):
        fib = j+k
        j = k
        if(i == 0):
            k +=1
        else:
            k = fib

    return fib
            

def factorial(num): 
    i = 1
    factorial = 1
    while(i<=num): 
        factorial = factorial*i
        i+=1

    return factorial
