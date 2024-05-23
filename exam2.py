def cal(n):
    if n < 0:
        print("Please enter a non-negative integer")
    elif n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

print(cal(5))





