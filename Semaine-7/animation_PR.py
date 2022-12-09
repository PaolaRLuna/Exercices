from time import sleep
import os

#iteresr a travers une liste de symbols
#por le lapin ajouter des variables et enlever

#Permet d'effacer ce qui est afficher à la console.
#Taken from https://stackoverflow.com/questions/2084508/clear-terminal-in-python
#By user: poke
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def alpaca_speaks():

#source: https://twitter.com/trillindagame/status/1072331174796763140?lang=en

    for i in range(5):
        #On efface la console pour chaque nouveau "frame" d'animation
        cls()
        space = ">"
        mouth = "o"
        if i == 1:
            space = ">"
            mouth = "ñ"
        elif i == 2:
            space = " "
            mouth = "-"
        elif i == 3:
            space = ">"
            mouth = "o"
        elif i == 4:
            space = " "
            mouth = "x"

        #Exemple sans animation
        print("                          ")
        print("          ∩~~∩           ")
        print("         ξ ･×･ ξ          ")
        print("         ξ　~  ξ          ")
        print("         ξ　   ξ          ")
        print("         ξ　   “~~~~~~O   ")
        print("         ξ　          ξ   ")
        print("         ξ ξ ξ~~ξ ξ       ")
        print("          ξ_ξξ_ξ ξ_ξξ_ξ   ")
        print("                          ")

        print(f""" 
                  ∩~~∩          
               {space}{space}ξ ･{mouth}･ ξ             
                 ξ　~  ξ
                 ξ　   ξ        
                 ξ　   “~~~~~~O         
                 ξ　          ξ   
                 ξ ξ ξ~~ξ ξ       
                  ξ_ξξ_ξ ξ_ξξ_ξ
                                  """)
        sleep(0.5)

alpaca_speaks()