
'''
Step 1: (Non-Decimal) Determine whether the desired base is within the current base's scope of numerals.
    If it is, while result >= 1, floor(num / desired) to get integer portion of numeral.

    If not, convert the desired base into the current base, then continue as above.

Step 2: (Decimal Portion) While
'''


from Acceptable_Divisor import Get_Acceptable_Divisor


def Iterative_Converter(current, desired, num):
    dividend = 0
    divisor = 0
    if Acceptable_Bases(current, desired):
        return
    else:
        divisor = Get_Acceptable_Divisor(current, desired)

    return


def Acceptable_Bases(current, desired):
    if desired > current:
        return False
    else:
        return True
