# on every year that is evenly divisible by 4
#   except every year that is evenly divisible by 100
#     unless the year is also evenly divisible by 400

def leap_year(year):
    # if year%4==0 and year%100!=0:
    #     if year%400==0:
    #         return True
    # elif year%4!=0:
    #     return False
    
    if year % 4 == 0:
        return True
    elif year % 4 != 0:
        return False
    elif year % 4 and year % 100 == 0:
        return False
    elif year % 4 and year % 100 != 0:
        return True
    elif year % 4 and year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 100 == 0 and year % 3 != 0:
        return False
    else:
        return False
