import unittest
from fibonacci import fibonacci
import sys
from io import StringIO

def fibonacci(n):
    if n <= 0:
        import sys
        sys.stderr.write("Число має бути додатнім\n")
        raise ValueError("Число має бути додатнім")
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a


class TestFibonacci(unittest.TestCase):

    def test_fibonacci_positive(self):
        self.assertEqual(fibonacci(1), 0)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 1)
        self.assertEqual(fibonacci(4), 2)
        self.assertEqual(fibonacci(5), 3)
        self.assertEqual(fibonacci(6), 5)
        self.assertEqual(fibonacci(7), 8)
        self.assertEqual(fibonacci(8), 13)

    def test_fibonacci_negative(self):
        with self.assertRaises(ValueError):
            fibonacci(0)
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_fibonacci_exit_code(self):
        saved_stdout = sys.stdout
        sys.stdout = StringIO(
        try:
            fibonacci(1)
        except SystemExit as e:
            self.assertEqual(e.code, 0)
        sys.stdout = saved_stdout

    def test_fibonacci_error_output(self)
        saved_stderr = sys.stderr
        sys.stderr = StringIO()
        with self.assertRaises(ValueError):
            fibonacci(-1)
        output = sys.stderr.getvalue().strip()
        print("Output:", output)  # Додано друк output
        self.assertNotEqual(output, "")
        self.assertEqual(output, "Число має бути додатнім")
        sys.stderr = saved_stderr


if __name__ == '__main__':
    unittest.main()

