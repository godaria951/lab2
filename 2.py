import os
import sys
from unittest import TestCase, main

def get_file_path(file_name):
    if not file_name:
        print("Error: File name not provided.", file=sys.stderr)
        return 1

    file_path = os.path.abspath(file_name)
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_name}' not found.", file=sys.stderr)
        return 2

    print(file_path)
    return 0

class TestGetFilePath(TestCase):
    def test_existing_file(self):
        self.assertEqual(get_file_path(__file__), 0)

    def test_nonexistent_file(self):
        self.assertNotEqual(get_file_path("nonexistent.txt"), 0)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = None

    sys.exit(get_file_path(file_name))