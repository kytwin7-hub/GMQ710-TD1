# Les données sont stockées dans un format spécial : elles sont encodées puis chiffrées,
# ce qui oblige à les déchiffrer avant de pouvoir les lire et les exploiter correctement.
import base64

# Nom du fichier contenant le contenu chiffré au format .grd.
filename = "data/raw/image_spuk.grd"

# Clé utilisée pour déchiffrer les données par opération XOR.
# La clé est stockée sous forme d'octets (bytes), ce qui est adapté à un chiffrement de type XOR.
key = b"datcha"

# Fonction qui applique un XOR entre chaque octet des données et la clé.
# On répète la clé autant de fois que nécessaire en utilisant l'index i.
def xor_data(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

# Lit le fichier, le décode depuis le format Base64,
# puis déchiffre les données avec XOR pour récupérer le texte brut.
def read_grid(filename):
    # Ouvre le fichier en mode binaire pour lire les octets bruts.
    with open(filename, "rb") as f:
        encoded_text = f.read()

    # Le fichier contient du texte encodé en Base64.
    # On le transforme donc en données binaires lisibles.
    encrypted_data = base64.b64decode(encoded_text)

    # Le XOR est utilisé pour inverser le chiffrement initial.
    decrypted_data = xor_data(encrypted_data, key)

    # On transforme les octets déchiffrés en texte UTF-8.
    # Le paramètre errors='ignore' évite de planter si le fichier contient
    # des caractères non valides ou des octets parasites.
    lines = decrypted_data.decode('utf-8', errors='ignore').splitlines()
    return lines

# On charge les lignes du fichier grille chiffré.
lines = read_grid(filename)

# combien de lignes avons-nous dans le fichier déchiffré ?
print(f"Nombre de lignes dans le fichier déchiffré : {len(lines)}")

# On affiche seulement les 13 premières lignes pour garder une sortie lisible.
for line in lines[:13]:
    print(line)

# -----------------------------------------------------------------------------
# Exemple de métadonnées du fichier GRID déchiffré :
# -----------------------------------------------------------------------------
# GRID_NAME: Sputnik_Satellite
# WIDTH: 100
# HEIGHT: 80
# PIXEL_SIZE: 300
# DATATYPE: uint16
# NODATA_VALUE: -1
# SENSOR: SPUKSat-1
# DATE_ACQUISITION: 1967-09-10
# BANDS: 3
# ...
# -----------------------------------------------------------------------------

# par la suite on devrait avoir des données (pixels), possiblement c'est après les métadonnées, 
# on pourrait avoir des valeurs représentant les pixels de l'image.

# imaginons on veut lire une ligne de données après les métadonnées, on pourrait faire quelque chose comme ça :
# choisissons une valeur arbitraire pour illustrer, par exemple la ligne 18 (en supposant que les lignes de données commencent après les métadonnées) :

pixels = lines[18] # on lit la ligne 18 par ex.

print(f"Ligne de données de pixels : {pixels}")
# 225 4 210 80 243 ... | 8 25 78 73 2 .... | 8 25 78 73 2 ...

# on voit le symbole | qui pourrait signifier la séparation entre les valeurs des bandes.

# combien y-a-t-il de symboles | dans cette ligne de données de pixels ?
num_bars = pixels.count('|')
print(f"Nombre de symboles '|' dans la ligne de données de pixels : {num_bars}")

# J'ai l'impression que chaque bande de l'image est séparée par le symbole |, ce qui pourrait indiquer que les valeurs des pixels pour chaque bande sont regroupées dans cette ligne.


# on pourrait certainement décomposer cette ligne en valeurs individuelles pour chaque bande, par exemple en utilisant la méthode split :
pixel_values = pixels.split('|')
print(f"Valeurs des pixels séparées : {pixel_values}")

# il semble que les lignes de données de pixels sont sous ce format :
# 10 10 20 ....| 20 50 10 .... | 20 50 30 ...
# 14 20 20 ....| 210 150 10 .... | 20 150 30 ...
# 100 12 200 ....| 20 250 10 .... | 120 50 30 ...
# ...

# autrement dit : 
# ligne 0 -> valeur_bande1|valeur_bande2|valeur_bande3
# ...

