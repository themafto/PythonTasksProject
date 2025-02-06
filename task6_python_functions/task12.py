import math

def generate_primes():
    x = 2
    while True:
        is_prime = True
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                is_prime = False
                break
        if is_prime:
            yield x
        x += 1

primes = generate_primes()
for ind, prime in enumerate(primes):
    if ind >= 10:  # Stop after 10 primes
        break
    print(prime)

