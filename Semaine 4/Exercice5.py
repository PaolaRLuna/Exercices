# Écrire un programme prenant l'année de naissance de l'utilisateur 
# et lui retournant sa génération. Vous pouvez utiliser la source 
# suivante: https://www.eurecia.com/blog/generations-x-y-z-sont-elles/

def generation():

    year = int(input("Entrer votre année de naissance: "))

    if 1946 <= year < 1965:
        return "Baby-boomer"
    elif 1965 <= year < 1980:
        return "Generation X"
    elif 1980 <= year < 2000:
        return "Generation Y"
    elif year > 2000:
        return "Generation Z"
    else:
        return "Vous êtes née avant 1946"
    
print(generation())

