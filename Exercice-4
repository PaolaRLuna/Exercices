# Exercice 4:

# Créez un programme demandant à un utilisateur d'entrer sa date de fête et retournez-lui 
# sa saison de naissance s'il est né dans l'hémisphère Nord. (Vous pouvez assumer que les 
# équinoxes et solstices ont lieu le 21 du mois.) 

def saison_naissance():
    jour_fete = int(input("Entrer votre jour de fête : "))
    mois_fete = int(input("Entrer votre mois de fête en nombre (ex. oct = 10) : "))
    
    if mois_fete in (1, 2):
        return "Votre saison est l'hiver"
    elif mois_fete in (4, 5):
        return "Votre saison est le printemps"
    elif mois_fete in (7, 8):
        return "Votre saison est l'ete"
    elif mois_fete in (10, 11):
        return "Votre saison est l'automne"
    else:
        if jour_fete <= 21 and mois_fete == 3:
            return "Votre saison est l'hiver"
        elif jour_fete > 21 and mois_fete == 3:
            return "Votre saison est le printemps"
        elif jour_fete <= 21 and mois_fete == 6:
            return "Votre saison est le printemps"
        elif jour_fete > 21 and mois_fete == 6:
            return "Votre saison est l'ete"
        elif jour_fete <= 21 and mois_fete == 9:
            return "Votre saison est l'ete"
        elif jour_fete > 21 and mois_fete == 9:
            return "Votre saison est l'automne"
        elif jour_fete <= 21 and mois_fete == 12:
            return "Votre saison est l'automne"
        elif jour_fete > 21 and mois_fete == 12:
            return "Votre saison est l'hiver"
        else:
            return "Ce n'est pas une date valide"


print(saison_naissance())


    
