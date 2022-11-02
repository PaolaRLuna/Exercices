# Exercice revue des pairs - Semaine 3
# Créer une calculatrice d'IMC demandant à l'utilisateur sa grandeur(en mètres), son poids(en kg). 
# Retournez ensuite la catégorie dans laquelle se trouve la personne.

# IMC = poids en kg/taille² (en m) 
# Source: https://sante.journaldesfemmes.fr/fiches-nutrition/2441413-comment-calculer-son-imc/

def imc_calcul():

    poids = int(input("Entrer votre poids (kg): "))
    taille = float(input("Entrer votre taille (m): "))

    imc = poids / taille ** 2
    
    if imc <= 18.5:
        return f"IMC: {imc:.1f}, vous êtes maigre"
    elif 18.5 < imc < 24.9:
        return f"IMC: {imc:.1f}, vous avez un poids normal"
    elif 25 < imc < 29.9:
        return f"IMC: {imc:.1f}, vous êtes en surpoids"
    elif imc > 30:
        return f"IMC: {imc:.1f}, vous êtes en obesité"

print(imc_calcul())