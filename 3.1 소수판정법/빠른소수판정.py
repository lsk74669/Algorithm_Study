def isPrime(N):
    LIMIT = int(N**0.5)
    for i in range(2, LIMIT + 1):
        if N % i == 0:
            return False
    return True

N = int(input())
if N >1 & isPrime(N):
    print('prime')
elif N == 1:
    print('not prime')
else:
    print('not prime')