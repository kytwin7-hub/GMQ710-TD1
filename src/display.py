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