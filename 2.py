import sys

def fibonacci(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

try:
    n = int(sys.stdin.readline())
    result = fibonacci(n)
    print(f"Число Фібоначчі для {n} дорівнює {result}")
except ValueError:
    sys.stderr.write("Будь ласка, введіть ціле число.\n")
    sys.exit(1)


