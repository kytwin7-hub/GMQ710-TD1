"""
src/process.py — Étape 2 : transformations

Responsabilité : séparer les métadonnées des données de pixels, et transformer les données de pixels en pseudo-matrice 2D.

"""

# on ne doit pas relire le fichier, on doit utiliser les lignes déjà lues par le module ingest.py
def extract_metadata(lines):
    """
    Sépare les métadonnées des données de pixels.

    """

    # une métadonnée est une ligne qui débute avec un # (c'est mon collègue qui m'a dit ça, je ne sais pas si c'est toujours vrai, mais on va faire comme ça pour l'instant).

    metadata = {}
    
    for line in lines:
        if line.startswith('#'):
            # exemple de métadonnée : # GRID_NAME: Sputnik_Satellite
            # on doit retirer le # et séparer la clé de la valeur
            line = line[1:].strip()  # on retire le # et les espaces autour
            # on vérifie si un : existe
            if ':' in line:
                key, value = line.split(':', 1)  # on sépare la clé de la valeur
                # si la clé existe déjà, on peut concaténer les valeurs
                if key.strip() in metadata:
                    metadata[key.strip()] += " " + value.strip()
                else:
                    metadata[key.strip()] = value.strip()  # on ajoute la métadonnée au dictionnaire
            
    # on retourne le dictionnaire des métadonnées
    return metadata

# on ne doit pas relire le fichier, on doit utiliser les lignes déjà lues par le module ingest.py
def extract_pixel_data(lines, band=0):
    """
    Transforme les données de pixels en pseudo-matrice 2D.

    """

    # pour les lignes de pixels, on va ignorer les lignes qui commencent par # (ce sont des métadonnées), et on va stocker les autres lignes dans une liste.
    pixel_data = []

    for line in lines:
        # ignore les lignes de métadonnées
        if not line.startswith('#'):
            # mon collègue m'a dit que les lignes de pixels sont sous ce format : 10 10 20 ....| 20 50 10 .... | 20 50 30 ...
            line = line.strip()  # on retire les espaces autour (nettoyage)
            if len(line) > 0:  # on ignore les lignes vides
                # on sépare les valeurs de la ligne
                data_bands = line.split(' | ')  # on sépare les valeurs de chaque bande

                # on récupère la bande demandée, on vérifie qu'elle existe
                if band < len(data_bands):
                    values = data_bands[band].split(' ')  # on sépare les valeurs de la bande
                    
                    pixel_data.append(values)  # on ajoute la ligne de pixels à la pseudo-matrice
                
    # je retourne la pseudo-matrice 2D des données de pixels
    # uniquement de la bande demandée (band)
    return pixel_data


