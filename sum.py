#sum of three numbers in python using function:
def sum_three(a, b, c):
    sum = a + b + c
    return sum
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
sum_result = sum_three(a, b, c)
print(f"sum of these three numbers = {sum_result}")