"""
Returns  x ^ exp
"""


from typing import Union


def to_power(x: Union[int, float], exp: int) -> Union[int, float]:
    if exp == 0:
        return 0
    if exp < 0:
        raise ValueError("This function works only with exp > 0.")
    if exp == 1:
        return x
    return x * to_power(x, exp-1)


dict_test = {2: 0, -3: 3, 3: 4, 5: -1}
for i, j in dict_test.items():
    print(to_power(i, j))
