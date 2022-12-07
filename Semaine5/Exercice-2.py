# def calculatrice(price_prod_past):
    
#     IPC_2021 = 141.6
#     IPC_1970 = 20.3
#     IPC_RATIO = IPC_2021/IPC_1970

#     print(IPC_RATIO)

#     prix_2021 = IPC_RATIO*price_prod_past
#     return price_prod_past, prix_2021


def read_file():

    with open("Semaine5/ipc.txt","r", encoding='utf8') as fichier:
        donnees = fichier.readlines()

        annee = []
        cpi = []
        #https://stackoverflow.com/questions/10711116/strip-spaces-tabs-newlines-python
        #Auteur: Rosstripi
        #replace tabs
        for donnee in donnees:
            donnee.replace('\t', ' ').replace('\n', '')
            donnees.append(donnee)
            #donnee.strip('/n')
        for i, ligne in enumerate(donnees):
            if i == 0:
                year = ligne.strip()
                annee.append(year)
            else:
                cpi.append(float(ligne))

        return annee, cpi

read_file()

# def create_datadict(donnees : list[str]):
#     donnees = read_file()

#     ipc = {}
#     for donnee in donnees:
#         annee, cpi = donnee.split(' ')
#         ipc[annee] = cpi



# def h_travail_par_produit(price_prod_past):
#     price_prod_1970, price_prod_2021 = calculatrice(price_prod_past)

#     WAGE_1970 = 1.65
#     WAGE_2021 = 15

#     hours_work_needed_1970 = price_prod_1970/WAGE_1970
#     hours_work_needed_2021 = price_prod_2021/WAGE_2021

#     return hours_work_needed_1970, hours_work_needed_2021, price_prod_2021

# def imprimer(price1970):
#     hrs_per_prod_1970, hrs_per_prod_2021, price2021 = h_travail_par_produit(price1970)
    
#     print(f"Un produit qui coutait {price1970} en 1970, coute {price2021:.2f} en 2021")
#     print(f"Le nombre d'hrs de travail pour payer un article en 1970 qui cout {price1970} est {hrs_per_prod_1970:.2f}")
#     print(f"Le nombre d'hrs de travail pour payer un article en 2021 qui cout {price2021:.2f} est {hrs_per_prod_2021:.2f}")


# imprimer(10)