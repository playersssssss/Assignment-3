def square_root(a, x_1, max_iterations=1000, tolerance=1e-6):
    x_n = x_1
    for i in range(max_iterations):
        x_n_plus_1 = 0.5 * (x_n + a / x_n)
        if abs(x_n_plus_1 - x_n) < tolerance:
            return x_n_plus_1
        x_n = x_n_plus_1
        return x_n  # Return the best guess if max_iteration is reached


# Get user input for the mnumber and initial guess
number = float(input("Enter a number to find its square root:"))
guess = float(input("Enter an initial for the square root:"))
# Calculate the square root using the iterative method
result = square_root(number, guess)
# print the result
print("Square root of", number, "is approximately:", result)
