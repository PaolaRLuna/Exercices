#Créer une liste de 5 éléments : [1, 2, 5, 3, 4]. Ensuite, créer deux 
# copies de cette liste, une copie en surface et une copie profonde 
# intitulée respectivement surface et profonde. Finalement, demander 
# à l'utilisateur d'entrer un mot, modifier le 2e élément de la liste 
# «surface» et le 3e élément de la liste «profonde» et imprimer les 
# trois listes à la console.

import copy

def changer_mot():

    cinq_e = [[1, 2, 5, 3, 4]]
    surface = copy.copy(cinq_e)
    profonde = copy.deepcopy(cinq_e)

    user_input = input("Entrer un mot: ")

    for elem in surface:
        elem[1] = user_input

    #surface[0][1] = user_input
    for elem in profonde:
        elem[2] = user_input

    #profonde[0][2] = user_input
    return f"{cinq_e}, \n {surface}, \n {profonde}"

print(changer_mot())