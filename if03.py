def main(a):
    """
    If the number is positive, increase it to 1,if the number is negative decrease it to 2.
    If it is 0, assign 10.
    Args:
        a: integer
    Returns:
        a: integer
    """
    k = a
    if k>0:
        k=k+1
    if k<0:
        k=k-2
    if k==0:
        k=10
    return k
a = 18
print(main(a))
a = -76
print(main(a))
a = 0
print(main(a))