def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"

    Args:
        temp: integer
    Returns:
        string: the message to print
    """
    s=""
    if temp<0:
        s="Freezing"
    if temp>0 and temp<10:
        s="Very Cold"
    if temp>11 and temp<=20:
        s="Cold"
    if temp>21  and temp<30:
        s="Normal"
    if temp>31 and temp<40:
        s="Hot"
    if temp>40:
        s="Very Hot"
    return s
a = 23
print(main(a))
a=56
print(main(a))
a=12
print(main(a))
a=8
print(main(a))
a=-9
print(main(a))