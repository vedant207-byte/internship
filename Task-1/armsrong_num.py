num = int(input("Enter a number:"))

num_str = str(num)
num_digits = len(num_str)

armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)

is_armstrong = (armstrong_sum == num)

print("Armstrong number:",is_armstrong)