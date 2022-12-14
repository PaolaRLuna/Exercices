class Point:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def distance(self, p2: "Point") -> float:
        #sqrt((x2-x1)^2 + (y2-y1)^2)
        dist_x = p2.x - self.x
        dist_y = p2.y - self.y
        dist = (dist_x ** 2 + dist_y ** 2) ** 0.5
        return dist

    def __add__(self, p2: "Point") -> "Point":
        return Point(p2.x + self.x, p2.y + self.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

class Point_3D(Point):
    def __init__(self, x, y, z) -> None:
        super().__init__(x, y)
        self.z = z

    def distance(self, p2: "Point_3D") -> float:
        dist_x = p2.x - self.x
        dist_y = p2.y - self.y
        dist_z = p2.z - self.z
        dist = (dist_x ** 2 + dist_y ** 2 + dist_z ** 2) ** 0.5
        return dist

    def __add__(self, p2: "Point_3D") -> "Point_3D":
        return Point_3D(p2.x + self.x, p2.y + self.y, p2.z +self.z)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

p1 = Point(1, 2)
p2 = Point(3, 5)
p3 = Point_3D(1, 2, 3)
p4 = Point_3D(2, 3, 4)
print(p1.distance(p2))
print(p1 + p2)
print(p3.distance(p4))
print(p3 + p4)
print(p3 + p1) #if we call p3 first it will throw an error because it hasnt been integrated into the self