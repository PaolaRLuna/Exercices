#  créez un programme permettant de recevoir une liste de données(en DMS) dans un fichier data.txt d'une taille 
# indéterminée et trouvez la position la plus proche du Pôle-Nord.

# Pour tester l'exécution de votre programme vous devez créer une liste ayant les positions en DMS d'au moins 10 
# villes et les placer dans le fichier data.txt.

def conversion_dms_dd(dms):  
    dd, mm, ss, dir = dms
    coeff = 1
    if dir == "S" or dir == "W" or dir == "O":
        coeff = -1
    return coeff * (dd + mm/60 + ss/3600)
     

def dist_deux_points(p_pole_nord, p_user):
    x1, y1 = p_user
    x2, y2 = p_pole_nord

    dist_x = x2 - x1 
    dist_y = y2 - y1

    dist = (dist_x**2 + dist_y**2) ** 0.5
    return dist

def distance_PN(position):
    PN_LAT = 86.50 #°N
    PN_LONG = 164.04 #°E
    PN = PN_LAT, PN_LONG

    lat, long = position
    lat_user_dd = conversion_dms_dd(lat)
    long_user_dd = conversion_dms_dd(long)
    position_dd = lat_user_dd, long_user_dd

    return dist_deux_points(PN, position_dd)

# def input_user():
#     def input_dms():
#         deg = int(input("Degrees: "))
#         min = int(input("Minutes: "))
#         sec = float(input("Secondes: ")
#         dir = input("Entrer direction (N, S, E, O): "))
#         return deg, min, sec, dir
    
#     print("Entrer longitude:")
#     longitude_dms = input_dms()
#     print("Entrer latitude: ")
#     latitude_dms = input_dms()
#     return longitude_dms, latitude_dms

# latitude_dms, longitude_dms = input_user()

latitude_dms = 45, 30, 31.99, "S" #45° 30' 31.9968'' N
longitude_dms = 73, 33, 42, "O"  #73° 33' 42.0048'' W
position = latitude_dms, longitude_dms

dist = distance_PN(position)
print(f"{dist:.3f}")