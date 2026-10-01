# Fichier d'entree principal du projet.
# C'est ce fichier qu'il faudra appeler principalement pour executer le programme.

# on peut s'inspirer de cet exemple :

# https://github.com/voirinprof/geo_pipeline_sample

# on peut essayer de séparer les fonctions 
# dans plusieurs modules : ingest.py, process.py, analyse.py, ...

# donc j'utiliserais le code de mon collègue pour le module ingest.py, et je vais l'importer ici.

from src.ingest import read_grid, display_raw
from src.process import extract_metadata, extract_pixel_data

# mon fichier
filename = "data/raw/image_spuk.grd"

# on va lire le fichier et récupérer les lignes déchiffrées
lines = read_grid(filename)

# on peut afficher le nombre de lignes pour vérifier que tout s'est bien passé
print(f"Nombre de lignes dans le fichier déchiffré : {len(lines)}")

# afficher les 10 premières lignes pour vérifier que tout s'est bien passé
display_raw(lines, num_lines=12)


# on va extraire les métadonnées et les données de pixels
metadata = extract_metadata(lines)
print(f"Nombre de lignes de métadonnées : {len(metadata)}")
print(metadata)
pixel_data = extract_pixel_data(lines, band=0)
print(f"Nombre de lignes de données de pixels : {len(pixel_data)}")
print(f"Nombre de colonnes de données de pixels : {len(pixel_data[0]) if len(pixel_data) > 0 else 0}")
#print(pixel_data)


