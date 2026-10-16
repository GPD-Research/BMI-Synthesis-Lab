from get_primes import get_first_n_primes_over

if __name__ == "__main__":
    primes = get_first_n_primes_over(100, 3)
    total_sum = sum(primes)
    print(f"Primes: {primes}")
    print(f"Sum of first three primes over 100: {total_sum}")