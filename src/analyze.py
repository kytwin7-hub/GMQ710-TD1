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

def identify_homogeneous_zones(pixel_data, nodata_value, threshold):
    visited = [[False for _ in row] for row in pixel_data]
    zones = []

    for row_index in range(len(pixel_data)):
        for col_index in range(len(pixel_data[0])):
            if not visited[row_index][col_index]:
                if pixel_data[row_index][col_index] == nodata_value:
                    visited[row_index][col_index] = True
                else:
                    zone = []
                    queue = [(row_index, col_index)]
                    start_value = pixel_data[row_index][col_index]
                    visited[row_index][col_index] = True

                    while queue:
                        current = queue.pop(0)
                        zone.append(current)

                        row, col = current

                        neighbors = [
                            (row - 1, col),
                            (row + 1, col),
                            (row, col - 1),
                            (row, col + 1),
                        ]

                        for n_row, n_col in neighbors:
                            if (0 <= n_row < len(pixel_data)
                                    and 0 <= n_col < len(pixel_data[0])
                                    and not visited[n_row][n_col]
                                    and pixel_data[n_row][n_col] != nodata_value
                                    and abs(pixel_data[n_row][n_col] - start_value) <= threshold):
                                 visited[n_row][n_col] = True
                                 queue.append((n_row, n_col))

                    zones.append(zone)

    return zones

def estimate_surface(zone, pixel_size):
    return len(zone) * pixel_size * pixel_size