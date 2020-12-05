from retireAgeCalc import *
from inputFunctions import getInt
def main():
    print("Social Security Full Retirement Age Calculator")
    while True:
        birthYear = getInt("Enter the year of birth or \"enter\" to exit: ")
        if birthYear == 1:
            break
        birthMonth = getInt("Enter the month of birth: ")
        retireYear, retireMonth = getFullRetireAge(birthYear)
        print("Your retirement age is", retireYear, "and", retireMonth,"months")
        retireYearDate, retireYearMonth = getFullRetireYearMonth(birthYear, birthMonth, retireYear, retireMonth)
        print("This will be", retireYearMonth, "of", retireYearDate)
main()

