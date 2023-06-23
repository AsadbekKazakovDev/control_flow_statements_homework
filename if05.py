def main(a,b,c):
    """
    Find number of negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    k = 0
    if a>0 and b>0 and c>0:
        k+=0
    if (a<0 and b>0 and c>0) or (a>0 and b<0 and c>0) or (a>0 and b>0 and c<0):
        k+=1
    if (a<0 and b<0 and c>0)or(a>0 and b<0 and c<0)or(a<0 and b>0 and c<0):
        k+=2
    if a<0 and b<0 and c<0:
        k+=3
    return k
a,b,c = 3 , 4 , -9
print(main(a,b,c))
a,b,c = -3,-9,8
print(main(a,b,c))
a,b,c = -8,-49,-78
print(main(a,b,c))
a,b,c = 9,3,6
print(main(a,b,c))