menu = { 1 : "Keven Presseau-St-Laurent - Concepts de programmation 1",
            2 : "Nicolas Thavonekham Robidoux - Logique mathématique pour l'informatique",
            3 : "Keven Presseau-St-Laurent - Systèmes d'exploitation",
            4 : "Anna Claudia Onofri - Anglais de niveau collégial"
            }

with open("Semaine-6/bdd", "w") as file:

        delimiter = ""
        for value in menu.values():
            cle = delimiter.join(i for i in value) + "\n"
            file.write(cle)
        