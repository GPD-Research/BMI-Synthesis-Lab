import decimal

def compute_pi_digits(num_decimals):
    # Set precision high enough to accurately get `num_decimals`
    decimal.getcontext().prec = num_decimals + 10
    
    # Chudnovsky algorithm or Gauss-Legendre for precision pi
    # For 50 decimals, standard high-precision Ramanujan/Chudnovsky works quickly:
    # Or using Machin-like formula: 16*atan(1/5) - 4*atan(1/239)
    def arctan(x):
        x = decimal.Decimal(x)
        x2 = x * x
        result = x
        term = x
        n = 1
        while term:
            term *= -x2
            n += 2
            next_term = term / n
            if not next_term:
                break
            result += next_term
        return result

    pi = 16 * arctan(5) ** -1 # Wait, atan(1/5) is arctan(Decimal(1)/5)
    # Let's write standard series for arctan(1/x):

def get_pi_machin(prec):
    decimal.getcontext().prec = prec + 10
    
    def arccot(x):
        x = decimal.Decimal(x)
        x2 = x * x
        result = decimal.Decimal(1) / x
        term = result
        n = 1
        while True:
            term = -term / x2
            n += 2
            delta = term / n
            if not delta:
                break
            result += delta
        return result

    pi = 4 * (4 * arccot(5) - arccot(239))
    return str(pi)

if __name__ == "__main__":
    pi_str = get_pi_machin(50)
    # Extract integer and decimal parts
    integer_part, decimal_part = pi_str.split('.')
    decimal_digits = decimal_part[:50]
    
    print(f"Pi: {integer_part}.{decimal_digits}")
    print("\nFirst 50 decimal digits of Pi:")
    for i, digit in enumerate(decimal_digits, start=1):
        print(f"Decimal position {i:2d}: {digit}")