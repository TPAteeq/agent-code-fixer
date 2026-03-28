from functions.run_python_file import run_python_file


def main():
    print("Test: main.py (usage instructions)")
    print(run_python_file("calculator", "main.py"))

    print("Test: main.py with args")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))

    print("Test: tests.py")
    print(run_python_file("calculator", "tests.py"))

    print("Test: ../main.py (should error)")
    print(run_python_file("calculator", "../main.py"))

    print("Test: nonexistent.py (should error)")
    print(run_python_file("calculator", "nonexistent.py"))

    print("Test: lorem.txt (should error)")
    print(run_python_file("calculator", "lorem.txt"))


if __name__ == "__main__":
    main()
