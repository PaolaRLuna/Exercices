# class C :
#     x = 23

# #
# a = C()

# a.x
# a.x = 12
# a.x

# C.x
# C.z = 6
# a.y = 44
# b = C()
# b.x
# b.z

# v = 5
# class C:
#     x = v+3
#     y = x + 1

# a = C()
# a.x
# a.x = 2 # pour l'objet
# a.x 
# C.x
# C.x = -1 
# #print(C.__dict__)
# dir(C)

# class C:
#     x = 23
#     y = x + 5
#     def affiche(self):
#         self.z = 42
#         print(C.y)
#         print(self.z)

# obj = C()
# obj.affiche

# class C:
#     def __init__(self, n):
#         self.x = n

# une_instance = C(42)
# une_instance.x

class Vecteur2D:
    def __init__(self, x0, y0):
        self.x = x0
        self.y = y0
    def __add__(self, second):
        return Vecteur2D(self.x + second.x, self.y + second.y)

    def __str__(self):
        return "Vecteur({:g}, {:g})".format(self.x, self.y)

v1 = Vecteur2D(1.2, 2.3)
v2 = Vecteur2D(3.4, 4.5)

print(v1 + v2)

