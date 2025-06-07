txt = input("Enter a string:")

is_palindrome = txt == txt[::-1]

print("palindrome:",is_palindrome)