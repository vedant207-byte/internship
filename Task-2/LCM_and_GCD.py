import math

def gcd_lcm(a, b):
    gcd = math.gcd(a, b)
    lcm = abs(a * b) // gcd
    return lcm, gcd

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
lcm, gcd = gcd_lcm(a, b)
print("LCM:", lcm)
print("GCD:", gcd)
