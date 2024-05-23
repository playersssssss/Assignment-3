def greater_common_divisor(A: int, B: int):
    # Using the Euclidean algorithm to compute the Greatest Common Divisor of two integers
    while B != 0:  # Continue looping while B is not equal to 0

        A, B = B, A % B  # A becomes B, and B becomes the remainder of A divided by B

    return A  # When B is 0, A is the Greatest Common Divisor


# Read two integers form user input
A = int(input("Please input the integer A :"))  # Prompt the user to input the first integer
B = int(input("Please input the integer B:"))  # Prompt the user to input the second integer
# call the greater_common_divisor function to compute the Greatest Common Divisor
result = greater_common_divisor(A, B)
# Output the Greatest Common Divisor
print("The greater common divisor is:", result)  # Print the result
