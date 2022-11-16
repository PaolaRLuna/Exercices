#  créez un programme permettant de recevoir une liste de données(en DMS) dans un fichier data.txt d'une taille 
# indéterminée et trouvez la position la plus proche du Pôle-Nord.

# Pour tester l'exécution de votre programme vous devez créer une liste ayant les positions en DMS d'au moins 10 
# villes et les placer dans le fichier data.txt.

#https://stackoverflow.com/questions/42376696/converting-specific-elements-in-a-list-of-lists-from-a-string-to-an-integer




def read_data():
    with open("Semaine5/coord.txt","r") as file:
        lines = file.readlines()
        donnees = []
        for line in lines:
            coord = line.split(", ")
            coord = coord[:-1]
            conversion_int = []
            for data in coord:
                if data.isdigit():
                    data = int(data)
                conversion_int.append(data)
                
            ville, latdd, latmm, latss, latdir, londd, lonmm, lonss, longdir = conversion_int
            latitude_dms = latdd, latmm, latss, latdir
            longitude_dms = londd, lonmm, lonss, longdir
            position = ville, latitude_dms, longitude_dms
            donnees.append(position)
    return 

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

    ville, lat, long = position
    lat_user_dd = conversion_dms_dd(lat)
    long_user_dd = conversion_dms_dd(long)
    position_dd = lat_user_dd, long_user_dd
    return dist_deux_points(PN, position_dd), ville

distance, ville = distance_PN(read_data())
print(f"{ville} {distance:.3f}")

f.close()
