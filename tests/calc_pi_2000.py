import decimal

def compute_pi_chudnovsky(digits):
    # Set context precision higher than requested digits to avoid rounding errors
    decimal.getcontext().prec = digits + 20

    C = 640320
    C3_OVER_24 = C**3 // 24

    def bs(a, b):
        if b - a == 1:
            if a == 0:
                P = Q = decimal.Decimal(1)
            else:
                P = decimal.Decimal((6 * a - 5) * (2 * a - 1) * (6 * a - 1))
                Q = decimal.Decimal(a * a * a * C3_OVER_24)
            T = P * (13591409 + 545140134 * a)
            if a & 1:
                T = -T
            return P, Q, T

        m = (a + b) // 2
        P_a, Q_a, T_a = bs(a, m)
        P_b, Q_b, T_b = bs(m, b)

        P = P_a * P_b
        Q = Q_a * Q_b
        T = Q_b * T_a + P_a * T_b
        return P, Q, T

    # Chudnovsky converges at ~14.18 digits per term
    terms = int(digits / 14.18) + 1
    P, Q, T = bs(0, terms)
    
    sqrt_C = decimal.Decimal(C).sqrt()
    pi = (Q * 426880 * sqrt_C) / T
    return pi

if __name__ == "__main__":
    digits = 2000
    pi_val = compute_pi_chudnovsky(digits)
    # Format to exact 2000 decimal places
    pi_str = str(pi_val)
    integer_part, decimal_part = pi_str.split('.')
    exact_2000_decimals = decimal_part[:digits]
    
    print(f"Pi calculated to {digits} decimal places:")
    print(f"{integer_part}.{exact_2000_decimals}")
    print(f"\nTotal Decimal Digits printed: {len(exact_2000_decimals)}")