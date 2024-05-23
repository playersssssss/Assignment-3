class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # operator overloading
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


vec1 = Vector(1, 2)
vec2 = Vector(3, 4)

vec_sum = vec1 + vec2

print(vec_sum)

