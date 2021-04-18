def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%400 == 0:
        leap = True
    elif year%400 == 0 and year%400 != 0:
        leap = False
    return leap

year = int(input())