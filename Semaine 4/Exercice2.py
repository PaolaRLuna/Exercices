# Créer un programme prenant en paramètre les conditions météorologiques suivantes:

# L'état du ciel(Ensoleillé, nuageux ou éclaircies), les précipitations (aucune, pluie, neige ou verglas), 
# la vitesse des vents en km/h et la température en C.

# Ensuite, affichez à l'écran un message d'alerte météorologique si les conditions suivantes sont respectées:

#     Il y a des précipitations et les vents sont supérieurs à 30 km/h
#     Il y a du verglas
#     Il fait soleil, mais les vents sont supérieurs à 70km/h ou les températures sont supérieures à 30C ou inférieures à -25C.
#     Il fait nuageux et les vents sont supérieurs à 50km/h.
#     Il fait nuageux et les vents sont supérieurs à 30km/h, mais la température est supérieure à 25C ou inférieure à -20C
#     Il neige et la température est inférieure à -25C.
#     Il fait ensoleillé, il n'y a pas de vent et la température est supérieure à 25C.

# Permettez à un utilisateur de rentrer les conditions météorologiques à l'aide d'un menu et assurez-vous 
# qu'il soit impossible de rentrer des conditions météorologiques qui ne font pas de sens.

# commencer par faire le menu

def meteo(etat_ciel, precip, vent, temp):
    def menu():
        def input_ciel():
            user_ciel = input("Entrer l'etat du ciel (ensoleille, nuageux ou eclaircies: ")
        
        def input_precip():
            user_precip = input("Entrer le type de precipitation (aucune, pluie, neige ou verglas: ")
        
        def input_vent():
            user_vent = input("Entrer la vitesse du vent en km/h: ")

        def input_temp():
            user_temp = input("Entrer la temperature en C: ")
            