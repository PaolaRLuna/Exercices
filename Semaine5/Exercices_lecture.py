# x, cpt = 257, 0
# sauve = x
# while x > 1:
#     x = x // 2
#     cpt = cpt + 1

# print("Approximation de log2 de ", sauve, ":", cpt)

# n = int(input("Entrez un entier "))
# while not (1<= n <= 10):
#     n = int


# for lettre in "ciao":
#     print(lettre, end="") # end va a imprimir todo en una linea en vez de imprimir cada objeto en una linea

# for x in range(1, 11):
#         if x == 5:
#             break
#         print(x, end="")

# y = int(input("Entrez un entier positif :"))
# while not(y > 0) :
#     y = int(input('Entrez un entier positif, S.V.P. : '))

# x = y // 2
# while x > 1:
#     if y % x == 0:
#         print(x, "a pour facteur", y)
#         break # voici l'interruption !
#     x -= 1
# else :
#     print(y, "est premier.")

# entiers = [2, 11, 8, 7, 5]
# cible = int(input("Entrez un entier :"))

# for entier in entiers:
#     if cible == entier:
#         print(cible, 'est dans la séquence', entiers)
#         break # voici l'interruption !
# else:
#     print(cible, "n'est pas dans la séquence", entiers)

#EXERCICES ______https://python.sdv.univ-paris-diderot.fr/05_boucles_comparaisons/_____

#5.4.1
# liste = ["vache", "souris", "levure", "bacterie"]
# for animal in liste:
#     print(animal)

# for i in range(len(liste)):
#     print(liste[i])

# i = 0
# while i < len(liste):
#     print(liste[i])
#     i += 1

# 5.4.2
# semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

# for jour in semaine:
#     print(jour)

# i = 5
# while i < len(semaine):
#     print(semaine[i])
#     i += 1

#5.4.3
# #range starts at 1 and stops at 11
# for i in range(1, 11):
#     print(i, end="")

# i = 1
# while i <= 10:
#     print(i, end="")
#     i +=1

#5.4.4 
# impairs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

# for i in impairs:
#     i = i + 1
#     print(i)

#5.4.5
# notes = [14, 9, 6, 8, 12]
# moyenne = sum(notes) / len(notes)
# print(f"{moyenne:.2f}")

# 5.4.6
#range(start, stop[, step])
# entiers = list(range(2,21,2))
# print(entiers)

# for i in entiers:
#     i = i * (i+2)
#     print(i)

#5.4.7
# i = 1
# while i <= 10:
#     star = i * "*"
#     print(star)
#     i +=1

#5.4.8
#range(start, stop[, step])
# for i in range(10,0,-1):
#     star = i * "*"
#     print(star)

#5.4.9
# for i in range(1,10,1):
#     star = i * "*"
#     print(f"{star:>10}")

    
#5.4.10
# i = 1
# while i <= 20:
#     star = i * "*"
#     print(f"{star:^20}")
#     i +=2

# reponse = input("Entrez un nombre de lignes (entier positif): ")
# N = int(reponse)

# i = 1
# while i <= N*2:
#     star = i * "*"
#     print(f"{star:^20}")
#     i +=2

#5.4.11

    # s = 0
    # i = 0.1
    # while i < 324000:
    # i = i * 2   
    # s = s + 1
    # print(i,s)
    # print(s)

# v = 100000
# for i in range(1,11):
#     v= v*1.01
#     print(i,v)

v = 100000
i = 0
while v < 200000:
    i = i+1
    v = v * 1.01
    print(i,v)
