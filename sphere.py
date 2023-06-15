import math

class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        return 4/3 * math.pi * self.radius ** 3


radius = float(input("Enter the radius of the sphere: "))
sphere = Sphere(radius)
print("The surface area of the sphere is:", sphere.surfaceArea())
print("The volume of the sphere is:", sphere.volume())
