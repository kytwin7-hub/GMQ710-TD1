"""
src/ingest.py — Étape 1 : chargement des données.

Responsabilité unique : obtenir les données brutes et les retourner
sous forme de Liste de listes. Aucune transformation ici.
"""


# Les données sont stockées dans un format spécial : elles sont encodées puis chiffrées,
# ce qui oblige à les déchiffrer avant de pouvoir les lire et les exploiter correctement.
import base64

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

def display_raw(lines, num_lines=10):
    """
    Affiche les premières lignes du fichier déchiffré pour vérification.

    """
    print(f"Nombre de lignes dans le fichier déchiffré : {len(lines)}")
    for line in lines[:num_lines]:
        print(line)
