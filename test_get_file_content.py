from functions.get_file_content import get_file_content


def main():
    print("Test: lorem.txt (should truncate at 10000 chars)")
    result = get_file_content("calculator", "lorem.txt")
    print(f"  Length: {len(result)}")
    print(f"  Ends with truncation message: {result.endswith(']')}")

    print("\nTest: calculator/main.py")
    result = get_file_content("calculator", "main.py")
    print(result)

    print("\nTest: calculator/pkg/calculator.py")
    result = get_file_content("calculator", "pkg/calculator.py")
    print(result)

    print("\nTest: /bin/cat (should return error)")
    result = get_file_content("calculator", "/bin/cat")
    print(result)

    print("\nTest: pkg/does_not_exist.py (should return error)")
    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(result)


if __name__ == "__main__":
    main()
