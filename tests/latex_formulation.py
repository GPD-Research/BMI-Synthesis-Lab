from get_primes import get_first_n_primes_over

if __name__ == "__main__":
    primes = get_first_n_primes_over(100, 3)
    total_sum = sum(primes)
    
    latex_eq = f"S = \\sum_{{i=1}}^{{3}} p_i = {primes[0]} + {primes[1]} + {primes[2]} = {total_sum}"
    print("LaTeX Equation Formulation:")
    print(latex_eq)