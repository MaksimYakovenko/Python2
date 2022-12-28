def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
def Isprime(n):
    i = 2
    j = 0
    while True:
        if i*i <= n and j != 1:
            if n % i == 0:
                j += 1
            i += 1
        elif j==1:
            return False
        else:
            return True

n = int(input('n='))

if n != 4 :
    print(fibonacci(n))
    
    if Isprime(fibonacci(n)) == True:
        print('Is Prime')
