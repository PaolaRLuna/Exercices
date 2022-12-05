from time import sleep
import os

#Permet d'effacer ce qui est afficher à la console.
#Taken from https://stackoverflow.com/questions/2084508/clear-terminal-in-python
#By user: poke
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def player_dead():

    for i in range(4):
        #On efface la console pour chaque nouveau "frame" d'animation
        cls()
        left = "O"
        right = "O"
        if i == 1:
            left = "0"
            right = "0"
        elif i == 2:
            left = "x"
            right = "x"
        elif i == 3:
            left = "-"
            right = "-"
        #Exemple sans animation
        print("          ******          ")
        print("         *      *         ")
        print("        *  O  O  *        ")
        print("        *   ^    *        ")
        print("         * ---- *         ")
        print("          ******          ")
        print("                          ")

        #Exemple animé avec l'utilisation de print f pour assigner des strings dynamiquement.
        #Remarquez que malgré que left et right prennent beaucoup d'espace dans le code l'affichage se fait correctement,
        #car ces variables ne représentent qu'un seul caractère lors de l'exécution.
        print(f""" 
                  ******          
                 *      *         
                *  {left}  {right}  *        
                *   ^    *        
                 * ---- *         
                  ******          
                                  """)
        
        #On doit faire dormir le système entre chaque animation, sinon les animations sont trop rapides et on ne les voit pas.
        sleep(0.5)

def move_right():

    space = "  "
    left = "O"
    right = "O"
    for i in range(10):
        cls()
        space = space + " "
        #Exemple sans animation
        print("          ******          ")
        print("         *      *         ")
        print("        *  O  O  *        ")
        print("        *   ^    *        ")
        print("         * ---- *         ")
        print("          ******          ")
        print("                          ")

        #Exemple animé avec l'utilisation de print f pour assigner des strings dynamiquement
        print(f""" 
        {space}           ******          
        {space}          *      *         
        {space}         *  {left}  {right}  *        
        {space}         *   ^    *        
        {space}          * ---- *         
        {space}           ******          
        {space}                           """)
        
        #On doit faire dormir le système entre chaque animation, sinon les animations sont trop rapides et on ne les voit pas.
        sleep(0.2)
def wave():
    wave = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    for i in range(len(wave)):
        cls()
        wave = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if i == 0:
            wave = "A" + wave[1:]
        elif 1 <= i <= (len(wave) - 2):
            wave = wave[:i] + "A" + wave[i+1:]
        else:
            wave = wave[:-2] + "A"
        print(wave)
        sleep(0.03)

def roll():
    for i in range(30):
        #cls()
        pos = i % 4
        player = ""
        if pos == 0:
            player = "|"
        if pos == 1:
            player = "/"
        if pos == 2:
            player = "-"
        if pos == 3:
            player = "\\"
        left_space = i * " "
        #Si vous voulez le faire sur une seule ligne vous pouvez
        #utiliser le caractère spécial \r, faire un print sans retour de ligne
        print('\r' + left_space + player, end='')
        sleep(0.1)
    #Il faut faire un retour de ligne à la fin pour afficher
    #le menu sur la ligne suivante. 
    #Vous pouvez aussi faire un clearscreen (cls())
    #print("\n")
    cls()
        
def menu():
    exit = False
    while not exit:
        print("Choisir une des animations suivantes: ")
        print("1. Le joueur meurt")
        print("2. Le joueur se déplace vers la droite")
        print("3. Faire une vague")
        print("4. Faire une roulade")
        print("5. Sortir du jeu")
        choix = int(input("Écrire votre choix: "))
        if choix == 1:
            player_dead()
        if choix == 2:
            move_right()
        if choix == 3:
            wave()
        if choix == 4:
            roll()
        if choix == 5:
            exit = True

menu()


