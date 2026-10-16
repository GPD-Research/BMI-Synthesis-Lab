def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_first_n_primes_over(threshold, count):
    primes = []
    candidate = threshold + 1
    while len(primes) < count:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes

if __name__ == "__main__":
    primes = get_first_n_primes_over(100, 3)
    print("First three primes over 100:", primes)