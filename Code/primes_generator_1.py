    
def is_prime(tryVal):
    factors = [divisor for divisor in range(2, tryVal) if tryVal % divisor == 0 ]
    return len(factors) == 0

def primes_to(maxVal):
    return [nextInt for nextInt in range(2, maxVal) if is_prime(nextInt)]

for prime in primes_to(100):
    print(prime)
