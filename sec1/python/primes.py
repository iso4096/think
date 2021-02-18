def generate_primes(no=100):
    primes = []
    for i in range(1, no+1):
        if i != 1:
            is_prime = True
            for prime in primes:
                if not i%prime:
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)
    return primes

print(generate_primes())