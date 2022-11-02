# Géolocation
# Vous travaillez sur un système de géolocation s'intitulant à la recherche du pôle Nord utilisant 
# des coordonnées sous la forme degrés minutes secondes (DMS).

# Pour faciliter l'utilisation du système, on vous demande de créer un court programme permettant 
# de convertir ces données sous la forme de degrés décimaux (DD).

# De plus, considérant que le but de l'application est d'indiquer la distance des usagers du pôle 
# Nord magnétique en plus d'indiquer leur position, on vous demande d'ajouter à votre programme 
# une fonction permettant de calculer cette distance.

# Versionner votre travail avec GitHub desktop et publié le sur votre profil GitHub Web une fois terminé.

# Source conversion: https://support.goldensoftware.com/hc/en-us/articles/228362688-Convert-Degrees-Minutes-Seconds-To-Decimal-Degrees-in-Strater
# Pole nord étant Point 2
#User position Point 1

def conversion_dd():
    dd, mm, ss = positiondms
    return dd + mm/60 + ss/3600
     


def dist_deux_points():
    # point 1
    #X1,y1

    lat_user, long_user = conversion_dd(positiondms)
    x1, y1 = long_user, lat_user

    #x2, y2
    PN_LAT = 86.50 #°N
    PN_LONG = 164.04 #°E
    x2, y2 = PN_LONG, PN_LAT

    dist_x = x2 - x1 
    dist_y = y2 - y1

    dist = (dist_x**2 + dist_y**2) ** 0.5
    return dist


latitude_dms = 45, 30, 31.99 #45° 30' 31.9968'' N
longitude_dms = 73, 33, 42  #73° 33' 42.0048'' W
positiondms = latitude_dms, longitude_dms

dist_deux_points()



# Exercice 6:

# En partant de l'exercice du système de géolocation, modifiez votre code pour que les positions 
# en DMS incluent la direction cardinale(N, S, E, W ou O) et retourne une position en DD pouvant 
# être négative. Modifiez ensuite votre code pour permettre à un utilisateur de manuellement 
# rentrer sa position.

