def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

n = int(input("Enter a number to find sum of its digits: "))
print("Sum of digits:", sum_of_digits(n))
