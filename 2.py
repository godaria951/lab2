def fibonacci(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

try:
    n = int(input("Введіть число n: "))
    result = fibonacci(n)
    print(f"Число Фібоначчі для {n} дорівнює {result}")
except ValueError:
    print("Будь ласка, введіть ціле число.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = None

    sys.exit(get_file_path(file_name))
