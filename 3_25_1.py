"""
Returns  x ^ exp
"""


from typing import Union, Optional


def to_power(x: Optional[Union[int, float]], exp: int) -> Optional[Union[int, float]]:
    if exp == 0:
        return 1
    if exp < 0:
        raise ValueError("This function works only with exp > 0.")

    return x * to_power(x, exp-1)


dict_test = {2: 0, -3: 3, 3: 4, 5: 1}
for i, j in dict_test.items():
    print(to_power(i, j))
