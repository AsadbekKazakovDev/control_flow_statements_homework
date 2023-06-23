def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    b = a//10
    c = a%10
    k = False
    j = c*10+b
    if j==a:
        k=True  
    return k
a = 45
print(main(a))
a = 33
print(main(a))
a = 43
print(main(a))