N = int(input())

LIMIT = int(N**0.5)
divisors = set()
for i in range(1, LIMIT + 1):
    if N % i == 0:
        divisors.update([i, N//i])

sorted_list = sorted(divisors)
for i in sorted_list:
    print(i)