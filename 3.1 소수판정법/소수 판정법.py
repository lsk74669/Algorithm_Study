def isprime(N):
    for i in range(2, N):
        if N % i == 0:
            return False    
    return True