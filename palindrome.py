import sys


def is_palindrome(text):
    return text.casefold() == text.casefold()[::-1]


if __name__ == "__main__":
    text = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("Enter a string: ")

    if is_palindrome(text):
        print("The string is a Palindrome")
    else:
        print("The string is not a Palindrome")