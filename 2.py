import sys

def fibonacci(n):
    if n <= 0:
        raise ValueError("Число має бути додатнім")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return a + b


if __name__ == "__main__":
    try:
        n = int(input())
        result = fibonacci(n)
        print(result)
        sys.exit(0)
    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)


