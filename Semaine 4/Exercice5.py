# Écrire un programme prenant l'année de naissance de l'utilisateur 
# et lui retournant sa génération. Vous pouvez utiliser la source 
# suivante: https://www.eurecia.com/blog/generations-x-y-z-sont-elles/

def generation():

    year = int(input("Entrer votre année de naissance: "))

    if 1946 < year < 1965:
        print("Baby-boomer")
    elif 1965 < year < 1980:
        print("Generation X")
    elif 1980 < year < 2000:
        print("Generation Y")
    elif year > 2000:
        print("Generation Z")
    else:
        print("Vous êtes née avant 1946")
