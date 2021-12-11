def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]

def run():
    print(is_palindrome(1000))

if __name__ == '__main__':
    run()


# mypy palindrome.py --check-untyped-defs (fora de usar mypy para ver los errores tipo lenguaje fuertemente tipado)
# palindrome.py:6: error: Argument 1 to "is_palindrome" has incompatible type "int"; expected "str"