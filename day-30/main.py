def factorial(n):
    if n ==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
    

print(factorial(5))  


def fibonacci(n):
    if n ==1:
        return 1
    
    elif n == 0:
        return 0
    
    else:                
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(3))
print(fibonacci(7))

# fibonacci(2)