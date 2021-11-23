"""
Checks if input string is Palindrome
"""


def is_palindrome(looking_str: str) -> bool:
    try:
        if len(looking_str) % 2 and looking_str[0] == looking_str[-1]:
            return is_palindrome(looking_str[1:-1])
        elif len(looking_str) > 1 and looking_str[0] == looking_str[-1]:
            return is_palindrome(looking_str[1:-1])
        elif len(looking_str) <= 1:
            return True
        else:
            return False
    except TypeError:
        print("Only string")


list_test = ['mom', 'sassas', 'o', 'maoam', 'maooamm']
for i in list_test:
    print(is_palindrome(i))

