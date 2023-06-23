def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    s=""
    if a>9 and a%2==0 and a<100:
        s="two-digit even number"
    if a>9 and a%2==1 and a<100:
        s = "two-digit odd number"
    if a>99 and a%2==0 and a<1000:
        s = "three-digit even number"
    if a>99 and a%2==1 and a<1000:
        s = "three-digit odd number"
    return s
a = 87
print(main(a))
a=985
print(main(a))
a=76
print(main(a))
a=578
print(main(a))