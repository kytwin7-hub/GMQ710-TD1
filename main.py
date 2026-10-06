from src.ingest import read_grid
from src.process import extract_metadata, extract_pixel_data, convert_to_numbers
from src.validate import (validate_file_path, validate_metadata,
                          validate_band_number, validate_dimensions)
from src.analyze import calculate_statistics
from src.display import normalize_data, apply_threshold, create_histogram
from src.utils import show_progress


THRESHOLD = 100
NB_CLASSES = 10


def main():
    # 1. Lire le chemin du fichier
    file_path = input("Chemin du fichier .grd : ")

    # 2. Vérifier l'existence du fichier
    if not validate_file_path(file_path):
        return

    # 3. Lire le fichier puis extraire les métadonnées
    lines = read_grid(file_path)
    metadata = extract_metadata(lines)

    if metadata is None:
        print("Erreur : métadonnées invalides.")
        return

    # 4. Vérifier les métadonnées
    if not validate_metadata(metadata):
        return

    # 5. Demander et vérifier le numéro de bande
    while True:
        band_text = input("Numéro de bande : ")
        if validate_band_number(band_text, metadata["BANDS"]):
            band = int(band_text)
            break

    # 6. Extraire les pixels de la bande depuis lines
    band_lines = extract_pixel_data(lines, band)

    if band_lines is None:
        print("Erreur : impossible d'extraire les pixels de la bande.")
        return

    # 7. Convertir les données en nombres
    pixel_data = convert_to_numbers(band_lines)

    if pixel_data is None:
        print("Erreur : impossible de convertir les pixels.")
        return

    # 8. Vérifier les dimensions
    if not validate_dimensions(
        pixel_data,
        metadata["WIDTH"],
        metadata["HEIGHT"]
    ):
        return

    # 9. Calculer les statistiques
    stats = calculate_statistics(
        pixel_data,
        metadata["NODATA_VALUE"]
    )

    if stats is None:
        return

    print("Statistiques :", stats)

    # 10. Normaliser les données
    normalized = normalize_data(
        pixel_data,
        stats["min"],
        stats["max"],
        metadata["NODATA_VALUE"]
    )

    # 11. Appliquer le seuil sur les données originales
    mask = apply_threshold(
        pixel_data,
        THRESHOLD,
        metadata["NODATA_VALUE"]
    )

    # 12. Créer l'histogramme
    histogram = create_histogram(
        pixel_data,
        stats["min"],
        stats["max"],
        metadata["NODATA_VALUE"],
        NB_CLASSES
    )

    print("Histogramme :", histogram)
    print("Masque :", mask)


main()