def sum_of_digits(digit_string: str) -> int:
    if type(digit_string) != str or digit_string[0].isalpha():
        raise ValueError("input string must be digit string")
    if len(digit_string) == 1:
        return int(digit_string)
    result = int(digit_string[0])
    return result + sum_of_digits(digit_string[1:])


list_test = ['045', '566', 'v34']
for i in list_test:
    print(sum_of_digits(i))
