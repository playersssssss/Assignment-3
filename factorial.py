# Create a function
def factorial_fuc(i: int):
    # defined the initial value of the result
    result = 1
    # use if loop to
    if i == 0 or i == 1:
        return 1
    elif i < 0:
        print("ERROR")
    else:
        for n in range(1, i + 1):
            result = result * n
    return result


print(factorial_fuc(5))
