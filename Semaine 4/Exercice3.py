def salutation():

    selection = int(input('Choisir un nombre de 1 à 3: '))

    if selection == 1:
        return 'Bonjour'
    elif selection == 2:
        return 'Au revoir'
    elif selection == 3:
        return 'À plus tard'
    else:
        return "Vous n'avez pas choisi le bon nombre"

print(salutation())
    