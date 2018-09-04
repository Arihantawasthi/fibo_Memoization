fibo_cache = {}

def fibonacci(n):
    #Check if there is any cache and return it.
    if n in fibo_cache:
        return fibo_cache[n]
    
    #Compute fibonacci number.
    if n == 1:
        value = 1
    if n == 2:
        value = 1

    if n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    #Store the value in cache and return it.
    fibo_cache[n] = value
    return value

n = int(input("Enter a positive number: "))
print(fibonacci(n))


