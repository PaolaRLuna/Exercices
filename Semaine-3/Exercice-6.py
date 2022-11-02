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


def conversion_dd(positiondms):
    dd, mm, ss = positiondms
    decimal_degrees = dd + mm/60 + ss/3600
    return decimal_degrees

#print(conversion_dd())
def dist_user_pn(position):
    lat_user = conversion_dd(latitude_dms)
    long_user = conversion_dd(longitude_dms)
    PN_LAT = 86.50 #°N
    PN_LONG = 164.04 #°E
    latitude_p_user = PN_LAT - lat_user
    longitude_p_user = PN_LONG - long_user
    return latitude_p_user, longitude_p_user

def dist_deux_points():
    distx = x2 - x1
    disty = y2 - y1
    dist = (distx**2 + disty**2) ** 0.5
    return dist


latitude_dms = 45, 30, 31.99 #45° 30' 31.9968'' N
longitude_dms = 73, 33, 42  #73° 33' 42.0048'' W
positiondms = Latitude_dms, Longitude_dms





# Exercice 6:

# En partant de l'exercice du système de géolocation, modifiez votre code pour que les positions 
# en DMS incluent la direction cardinale(N, S, E, W ou O) et retourne une position en DD pouvant 
# être négative. Modifiez ensuite votre code pour permettre à un utilisateur de manuellement 
# rentrer sa position.

