from src.ingest import read_grid
from src.process import extract_metadata, extract_pixel_data, convert_to_numbers
from src.validate import (
    validate_file_path,
    validate_metadata,
    validate_band_number,
    validate_dimensions
)
from src.analyze import (
    calculate_statistics,
    identify_homogeneous_zones,
    estimate_surface
)
from src.display import normalize_data, apply_threshold, create_histogram
from src.utils import show_progress


THRESHOLD = 100
ZONE_THRESHOLD = 50
NB_CLASSES = 10
TOTAL_STEPS = 9


def main():
    show_progress(1, TOTAL_STEPS, "Saisie du chemin du fichier")
    file_path = input("Chemin du fichier .grd : ")

    show_progress(2, TOTAL_STEPS, "Vérification du chemin")

    if not validate_file_path(file_path):
        return

    show_progress(3, TOTAL_STEPS, "Lecture du fichier")
    lines = read_grid(file_path)

    show_progress(4, TOTAL_STEPS, "Extraction des métadonnées")
    metadata = extract_metadata(lines)

    if metadata is None:
        print("Erreur : métadonnées invalides.")
        return

    if not validate_metadata(metadata):
        return

    show_progress(5, TOTAL_STEPS, "Choix de la bande")

    while True:
        band_text = input("Numéro de bande : ")

        if validate_band_number(band_text, metadata["BANDS"]):
            band = int(band_text)
            break

    show_progress(6, TOTAL_STEPS, "Extraction et conversion des pixels")
    band_lines = extract_pixel_data(lines, band)

    if band_lines is None:
        print("Erreur : impossible d'extraire les pixels.")
        return

    pixel_data = convert_to_numbers(band_lines)

    if pixel_data is None:
        print("Erreur : impossible de convertir les pixels.")
        return

    if not validate_dimensions(
        pixel_data,
        metadata["WIDTH"],
        metadata["HEIGHT"]
    ):
        return

    show_progress(7, TOTAL_STEPS, "Calcul des statistiques")
    stats = calculate_statistics(
        pixel_data,
        metadata["NODATA_VALUE"]
    )

    if stats is None:
        return

    print("Statistiques :", stats)

    normalized = normalize_data(
        pixel_data,
        stats["min"],
        stats["max"],
        metadata["NODATA_VALUE"]
    )

    mask = apply_threshold(
        pixel_data,
        THRESHOLD,
        metadata["NODATA_VALUE"]
    )

    histogram = create_histogram(
        pixel_data,
        stats["min"],
        stats["max"],
        metadata["NODATA_VALUE"],
        NB_CLASSES
    )

    nb_masque = sum(sum(row) for row in mask)

    print("Histogramme :", histogram)
    print("Masque :", nb_masque, "pixels >= seuil", THRESHOLD)

    show_progress(8, TOTAL_STEPS, "Recherche des zones homogènes")
    zones = identify_homogeneous_zones(
        pixel_data,
        metadata["NODATA_VALUE"],
        ZONE_THRESHOLD
    )

    if len(zones) == 0:
        print("Aucune zone trouvée.")
        return

    show_progress(9, TOTAL_STEPS, "Calcul de la plus grande zone")
    biggest_zone = max(zones, key=len)

    surface = estimate_surface(
        biggest_zone,
        metadata["PIXEL_SIZE"]
    )

    print("Nombre de zones :", len(zones))
    print("Plus grande zone :", len(biggest_zone), "pixels")
    print("Surface :", surface)


if __name__ == "__main__":
    main()