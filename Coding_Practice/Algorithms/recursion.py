def factorial(n: int):
    if n == 1:
        return 1
    
    return n * factorial(n - 1)

def bunnyEars(n:int):
    if n == 0:
        return 0
    
    return 2 + bunnyEars(n - 1)

def fibonacci(n: int):
    if n == 0:
        return 0
    
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

def bunnyEars2(n: int):
    if n == 0:
        return 0
    if n % 2 == 0:
        return 3 + bunnyEars2(n - 1)
    else:
        return 2 + bunnyEars2(n - 1)

def triangle(n: int):
    if n == 0:
        return 0

    return n + triangle(n - 1) 

def sumDigits(n:int):
    if n % 10 == n // (10 * len(str(n))):
        return n % 10

    return n % 10 + sumDigits(n // 10)

def count7(n: int):
    if n % 10 == n // (10 * len(str(n))):
        if n == 7:
            return 1
        else: 
            return 0
    
    s = n % 10
    
    if s == 7:
        return 1 + count7(n // 10)

    else:
        return 0 + count7(n // 10)  

def count8(n: int):
    if n % 10 == n // (10 * len(str(n))):
        if n == 8:
            return 1
        else: 
            return 0
    
    s = n % 10
    
    if s == 8:
        return 1 + count8(n // 10)

    elif s == 8 and count8(n // 10):
        return 2 + count8(n // 10)

    else:
        return 0 + count8(n // 10)  

def allStar(word: str):
    pass

print(count8(8818))
