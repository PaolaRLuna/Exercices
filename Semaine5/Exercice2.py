# Créer une calculatrice permettant de calculer combien couteraient en 2021, 
# un article acheté en 1970. Utilisez le IPC moyenne annuelle de ces années respectives. 
# Les données sont disponibles ici: 
# https://www150.statcan.gc.ca/n1/pub/71-607-x/2018016/cpilg-ipcgl-fra.htm

# Vous pouvez comparer vos résultats ici: 
# https://www.banqueducanada.ca/taux/renseignements-complementaires/feuille-de-calcul-de-linflation/

#Indices

def calculatrice():
    #taux_moy_inflation = 3.95
    poucentage = 7.48529

    prix = 10
    prix_2022 = prix * poucentage
    return prix_2022

print(calculatrice())
