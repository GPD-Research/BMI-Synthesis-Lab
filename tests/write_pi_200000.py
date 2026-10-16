import decimal
import sys
import os

# Increase max string conversion limit for large numbers
sys.set_int_max_str_digits(500000)

def compute_pi_chudnovsky(digits):
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

    terms = int(digits / 14.18) + 1
    P, Q, T = bs(0, terms)
    
    sqrt_C = decimal.Decimal(C).sqrt()
    pi = (Q * 426880 * sqrt_C) / T
    return pi

if __name__ == "__main__":
    digits = 200000
    pi_val = compute_pi_chudnovsky(digits)
    pi_str = str(pi_val)
    integer_part, decimal_part = pi_str.split('.')
    exact_pi = f"{integer_part}.{decimal_part[:digits]}"

    output_path = "pi_200000.txt"
    with open(output_path, "w") as f:
        f.write(exact_pi + "\n")
        
    print(f"Successfully calculated and wrote pi to {output_path}")
    print(f"File size: {os.path.getsize(output_path)} bytes")