# function to calculate factorial
def factorial(n):
    result = 1
    if n == 0 or n == 1:
        result
    elif n < 0:
        print("ERROR")
    else:
        for i in range(1, n + 1):
            result = result * i

    return result


print(factorial(5))
