def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Replace 'number' with the desired number to find its factorial
number = int(input("enter a number:"))
result = factorial(number)
print(f"The factorial of {number} is: {result}")
