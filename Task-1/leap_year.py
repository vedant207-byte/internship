def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

try:
    year = int(input("Enter a year: "))
    if is_leap_year(year):
        print("True")
    else:
        print("False")
except ValueError:
    print("Please enter a valid integer year.")
