def getFullRetireAge(year):
    if (year <= 1937):
        return 65, 0
    elif (year == 1938):
        return 65, 2
    elif (year == 1939):
        return 65, 4
    elif (year == 1940):
        return 65, 6
    elif (year == 1941):
        return 65, 8
    elif (year == 1942):
        return 65, 10
    elif (year >= 1943) and (year <= 1954):
        return 66, 0
    elif (year == 1955):
        return 66, 2
    elif (year == 1956):
        return 66, 4
    elif (year == 1957):
        return 66, 6
    elif (year == 1958):
        return 66, 8
    elif (year == 1959):
        return 66, 10
    else:
        return 67, 0

def getFullRetireYearMonth(birthYear, birthMonth, retireYear, retireMonth):
    retireYearDate = birthYear + retireYear
    retireMonthDate = birthMonth
    while retireMonth > 0:
        retireMonthDate += 1
        retireMonth -= 1
        if retireMonthDate > 12:
            retireMonthDate = 1
            retireYearDate += 1
    return retireYearDate, getMonthName(retireMonthDate)

def getMonthName(retireMonthDate):
    if retireMonthDate == 1:
        return "January"
    elif retireMonthDate == 2:
        return "February"
    elif retireMonthDate == 3:
        return "March"
    elif retireMonthDate == 4:
        return "April"
    elif retireMonthDate == 5:
        return "May"
    elif retireMonthDate == 6:
        return "June"
    elif retireMonthDate == 7:
        return "July"
    elif retireMonthDate == 8:
        return "August"
    elif retireMonthDate == 9:
        return "September"
    elif retireMonthDate == 10:
        return "October"
    elif retireMonthDate == 11:
        return "November"
    elif retireMonthDate == 12:
        return "December"
    else:
        return "Error"
    

