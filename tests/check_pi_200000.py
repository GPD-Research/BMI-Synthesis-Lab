with open("pi_200000.txt", "r") as f:
    pi_content = f.read().strip()

integer_part, decimal_part = pi_content.split('.')
last_100_digits = decimal_part[-100:]

print(f"Total digits in file: {len(decimal_part)}")
print(f"Digits 199,901 to 200,000:\n{last_100_digits}")