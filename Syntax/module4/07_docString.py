#must be fist string in the function
def is_even(x):
    """
    find if number is even
    :param num:
    x: The number to check
    :return:
    True is number is even otherwise False
    """
    if x % 2:
        return False
    else:
        return True

print(is_even(5))
print(is_even(44))

print(help(is_even))

print(is_even.__doc__)