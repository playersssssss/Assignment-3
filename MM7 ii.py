class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

# Creating vectors
v1 = Vector(1, 2)
v2 = Vector(3, 4)

# Adding vectors
result = v1 + v2
print("Resultant Vector:", result.x, result.y)  # Output: Resultant Vector: 4 6
