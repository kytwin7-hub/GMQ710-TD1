def normalize_data(pixel_data, min_value, max_value, nodata_value):
    """Normalise les valeurs entre 0 et 1 (NODATA est conservé tel quel)."""

    if max_value == min_value:
        print("Erreur : toutes les valeurs sont identiques, normalisation impossible.")
        return None

    normalized = []
    for row in pixel_data:
        new_row = []
        for value in row:
            if value == nodata_value:
                new_row.append(nodata_value)
            else:
                new_row.append((value - min_value) / (max_value - min_value))
        normalized.append(new_row)

    return normalized


def apply_threshold(pixel_data, threshold, nodata_value):
    """Applique un masque : 1 si la valeur >= seuil, sinon 0 (NODATA donne 0)."""

    mask = []
    for row in pixel_data:
        new_row = []
        for value in row:
            if value == nodata_value:
                new_row.append(0)
            elif value >= threshold:
                new_row.append(1)
            else:
                new_row.append(0)
        mask.append(new_row)

    return mask


def create_histogram(pixel_data, min_value, max_value, nodata_value, nb_classes):
    """Compte le nombre de valeurs dans chaque classe (NODATA est ignoré)."""

    if max_value == min_value:
        print("Erreur : toutes les valeurs sont identiques, histogramme impossible.")
        return None

    counts = [0] * nb_classes

    for row in pixel_data:
        for value in row:
            if value == nodata_value:
                continue

            index = int((value - min_value) / (max_value - min_value) * nb_classes)

            if index == nb_classes:
                index = nb_classes - 1

            counts[index] += 1

    return counts