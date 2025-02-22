def is_year_leap(year):
    if (year % 4 == 0 and year % 400 == 0):
        return True
    else:
        return False

