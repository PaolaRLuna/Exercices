# Offrir à l'utilisateur d'entrer un nom de fichier et un nombre illimité de nombres positifs, tant et aussi longtemps qu'il ne rentre pas un nombre négatif. 
# Ajouter les nombres entrés par l'utilisateur à une liste en excluant le nombre négatif. Ensuite, écrire les résultats suivants dans le fichier nommé par l'utilisateur:

# La liste en ordre croissant
# La liste en ordre décroissant
# Le maximum
# Le minimum
# La moyenne de la liste
# La médiane (la valeur à la position centrale si la longueur de la liste est impaire et la moyenne des deux valeurs centrales si paire)
# Ex: 1, 2, 3, 5, 4. Médiane = 3.
# Ex: 1, 2, 3, 4, 5, 6. Médiane = 3.5
# Le mode (l'occurrence la plus fréquente s'il y a lieu. Si chaque entrée est unique, inscrire que le mode = none)
# Ex: 1, 2, 2, 2, 3, 4, 3, 4. La mode = 2

#Inspiration: https://stackoverflow.com/questions/31593212/how-to-take-any-number-of-inputs-in-python-without-defining-any-limit
#https://stackoverflow.com/questions/3011680/take-user-input-and-put-it-into-a-file-in-python
# https://stackoverflow.com/questions/66333471/read-and-save-list-of-numbers-as-numbers-in-txt-files-in-python
#https://stackoverflow.com/questions/7368789/convert-all-strings-in-a-list-to-int
#https://stackoverflow.com/questions/45388927/sorting-one-list-without-sorted-function
#https://www.geeksforgeeks.org/find-average-list-python/
#https://stackoverflow.com/questions/24101524/finding-median-of-list-in-python
#https://stackoverflow.com/questions/10797819/finding-the-mode-of-a-list
#https://stackoverflow.com/questions/3496518/using-a-dictionary-to-count-the-items-in-a-list
#https://datascienceparichay.com/article/python-count-occurrences-of-value-in-dictionary/

def create_input():

    filename = input("Entrer un nom de fichier: ")
    with open(filename, "w") as file:

        inputs = []
        #condition = False
        while True:
            u_input = input("Entre un nombre positif: ")

            if u_input == "":
                break #condition = True
            elif int(u_input) > 0:
                inputs.append(str(u_input))
            else:
                True

        delimiter = ","
        for item in inputs:
            value = delimiter.join(i for i in item) + "\n"
            file.write(value)

        inputs = [int(i) for i in inputs]
    return inputs


def croissant(donnees: list[int]):

    donnees = create_input()
    for donnee in range(0, len(donnees)-1):
        for item in range(0, len(donnees)- donnee - 1):
            if donnees[item] > donnees[item+1]:
                num = donnees[item]
                donnees[item] = donnees[item+1]
                donnees[item+1] = num

    return donnees


def decroissant(donnees: list[int]):

    donnees = create_input()
    for donnee in range(0, len(donnees)-1):
        for item in range(0, len(donnees)- donnee - 1):
            if donnees[item] < donnees[item+1]:
                num = donnees[item]
                donnees[item] = donnees[item+1]
                donnees[item+1] = num

    return donnees


def maximum(donnees: list[int]):

    donnees = create_input()
    max_number = donnees[0]

    for donnee in donnees:
        if donnee > max_number:
            max_number = donnee
    return max_number


def minimum(donnees: list[int]):

    donnees = create_input()
    min_number = donnees[0]
    
    for donnee in donnees:
        if donnee < min_number:
            min_number = donnee
    return min_number

def moyenne():
    donnees = create_input()
    moyenne = sum(donnees) / len(donnees)
    return moyenne

def mediane():

    donnees = croissant()
    long_d = len(donnees)
    index = (long_d - 1) // 2

    if long_d % 2 == 0:
        return (donnees[index] + donnees[index + 1]) / 2
    else:
        return donnees[index]

def mode(donnees: list[int]):

    counts = {}
    for donnee in donnees:
        counts[donnee] = counts.get(donnee, 0) + 1

    maxcount = 0
    lamode = None
    for cle, v in counts.items():
        if v > maxcount:
            lamode = cle
            maxcount = v

    count_val = 0
    for v in counts.values():
        if v >= 2:
            count_val += 1
        
    if maxcount == 1:
        return "None"
    elif count_val >= 2:
        return "List has multiple modes"
    else:
        return f"Mode of the list:", lamode

def output():
    



if __name__ == '__main__':
    output()
