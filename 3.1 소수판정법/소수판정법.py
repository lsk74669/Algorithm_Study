def isPrime(N):
    for i in range(2, N):
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