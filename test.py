import math
def find_a_b_sums(n):
    solutions = set()
    max_val = math.isqrt(n)
    for a in range(-max_val, max_val + 1):
        remainder = n - a * a
        if remainder < 0:
            continue
        b0 = math.isqrt(remainder)
        if b0 * b0 == remainder:
            solutions.add(a + b0)
            solutions.add(a - b0)
    return solutions
n = 4068
sums = find_a_b_sums(n)
print(f"all possible result: {sums}")