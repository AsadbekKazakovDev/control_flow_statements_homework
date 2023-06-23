def main(a,b,c):
    """
    Find number of positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
    k=0
    if a>0 and b>0 and c>0:
        k+=3
    if (a>0 and b>0 and c<0) or (a>0 and b<0 and c>0) or (a<0 and b>0 and c>0):
        k+=2
    if (a>0 and b<0 and c<0) or (a<0 and b<0 and c>0) or (a<0 and b>0 and c<0):
        k+=1
    return k
a,b,c = 3,2,-1
print(main(a,b,c))
a,b,c = 4,-2,-6
print(main(a,b,c))
a,b,c = 1,7,9
print(main(a,b,c))