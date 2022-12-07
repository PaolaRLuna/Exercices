# Créer une calculatrice permettant de calculer combien couteraient en 2021, 
# un article acheté en 1970. Utilisez le IPC moyenne annuelle de ces années respectives. 
# Les données sont disponibles ici: 
# https://www150.statcan.gc.ca/n1/pub/71-607-x/2018016/cpilg-ipcgl-fra.htm

# Vous pouvez comparer vos résultats ici: 
# https://www.banqueducanada.ca/taux/renseignements-complementaires/feuille-de-calcul-de-linflation/

#Indices
#Cost of products or services in a current period / cost of products or services in a previous time period x 100 = consumer price index
#cpi = ((current price/ past price)x 100)-100 in case we wanted %

#cost product 2021 = (cpi/100)*past price

def calculatrice(price_prod_past):
    #taux_moy_inflation = 3.95
    
    IPC_2021 = 141.6
    IPC_1970 = 20.3
    IPC_RATIO = IPC_2021/IPC_1970

    print(IPC_RATIO)

    prix_2021 = IPC_RATIO*price_prod_past
    #prix_2022 = IPC_1970_2021/100 * PAST_PRICE
    return price_prod_past, prix_2021


# Partie 2:

# En utilisant le salaire minimum de ces années respectives, affichez le résultat en nombre d'heures de travail.
#  Vous pouvez utiliser le salaire minimum fédéral ou provincial, tant que vous restez constant.
# https://srv116.services.gc.ca/dimt-wid/sm-mw/rpt2.aspx

# def heures_travail():
#     WAGE_1970 = 1.65
#     WAGE_2021 = 15

# Partie 3:

# Ensuite, comparez le nombre d'heures de travail nécessaire pour payer l'article au salaire minimum en 1970, en 2021 en fonction
#  du coût de 1970 ajusté pour l'inflation et en fonction de son coût en 2021. Faites attention d'utiliser le bon salaire minimum 
# dans vos calculs, pour le nombre d'heures en 1970, utilisez le salaire de 1970, alors que pour le nombre d'heures en 2016, utilisez 
# le salaire minimum de 2021.

def h_travail_par_produit(price_prod_past):
    price_prod_1970, price_prod_2021 = calculatrice(price_prod_past)

    WAGE_1970 = 1.65
    WAGE_2021 = 15

    hours_work_needed_1970 = price_prod_1970/WAGE_1970
    hours_work_needed_2021 = price_prod_2021/WAGE_2021

    return hours_work_needed_1970, hours_work_needed_2021, price_prod_2021

def imprimer(price1970):
    hrs_per_prod_1970, hrs_per_prod_2021, price2021 = h_travail_par_produit(price1970)
    
    print(f"Un produit qui coutait {price1970} en 1970, coute {price2021:.2f} en 2021")
    print(f"Le nombre d'hrs de travail pour payer un article en 1970 qui cout {price1970} est {hrs_per_prod_1970:.2f}")
    print(f"Le nombre d'hrs de travail pour payer un article en 2021 qui cout {price2021:.2f} est {hrs_per_prod_2021:.2f}")


imprimer(10)