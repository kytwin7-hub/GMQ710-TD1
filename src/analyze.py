"""
src/analyze.py — Étape 3 : calculs et statistiques .

Responsabilité : produire des métriques à partir des données traitées.

"""

def calculate_statistics(pixel_data, nodata_value):
    """Calcule le minimum, le maximum et la moyenne en ignorant NODATA."""

    valid_values = []
    for row in pixel_data:
        for value in row:
            if value != nodata_value:
                valid_values.append(value)

    if len(valid_values) == 0:
        print("Erreur : aucune valeur valide pour calculer les statistiques.")
        return None

    return {
        "min": min(valid_values),
        "max": max(valid_values),
        "mean": sum(valid_values) / len(valid_values),
    }