import random

def IsPrimeNumber(N):
    if N <= 1:
        return False
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return False
    return True

for _ in range(5):
    N = random.randint(1, 100)
    print(f"Число {N} является простым: {IsPrimeNumber(N)}")