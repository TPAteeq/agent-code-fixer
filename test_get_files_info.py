from functions.get_files_info import get_files_info 


def main():
    print("Result for current directory:")
    result = get_files_info("calculator", ".")
    print(format_output(result))

    print("\nResult for 'pkg' directory:")
    result = get_files_info("calculator", "pkg")
    print(format_output(result))

    print("\nResult for '/bin' directory:")
    result = get_files_info("calculator", "/bin")
    print(format_output(result))

    print("\nResult for '../' directory:")
    result = get_files_info("calculator", "../")
    print(format_output(result))


def format_output(result):
    if result.startswith("Error:"):
        return f"    {result}"
    
    return "\n".join(f"  {line}" for line in result.split("\n"))


if __name__ == "__main__":
    main()