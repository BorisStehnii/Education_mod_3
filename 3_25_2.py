"""
Checks if input string is Palindrome
"""


def is_palindrome(looking_str: str) -> bool:
    try:
        return len(looking_str) <= 1 or looking_str[0] == looking_str[-1] and is_palindrome(looking_str[1:-1])
    except TypeError:
        print("Only string")


list_test = ['mom', 'sassas', 'o', 'maoam', 'maooamm']
for i in list_test:
    print(is_palindrome(i))

