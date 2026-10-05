def validate_file_path(path):
    """Vérifie que le fichier existe et qu'il peut être ouvert."""
    try:
        with open(path, "rb"):
            pass
    except OSError:
        print("Erreur : impossible d'ouvrir le fichier :", path)
        return False

    return True


def validate_metadata(metadata):
    """Vérifie et convertit les métadonnées nécessaires."""

    required_keys = [
        "WIDTH",
        "HEIGHT",
        "BANDS",
        "PIXEL_SIZE",
        "DATATYPE",
        "NODATA_VALUE"
    ]

    # R2 : vérifier la présence des clés obligatoires
    for key in required_keys:
        if key not in metadata:
            print("Erreur : la métadonnée", key, "est absente.")
            return False

    # R3 : convertir WIDTH, HEIGHT et BANDS en nombres entiers
    for key in ["WIDTH", "HEIGHT", "BANDS"]:
        try:
            metadata[key] = int(metadata[key])
        except (ValueError, TypeError):
            print("Erreur :", key, "doit être un nombre entier.")
            return False

    # R3 : convertir PIXEL_SIZE en nombre décimal
    try:
        metadata["PIXEL_SIZE"] = float(metadata["PIXEL_SIZE"])
    except (ValueError, TypeError):
        print("Erreur : PIXEL_SIZE doit être un nombre.")
        return False

    # Convertir NODATA_VALUE en nombre entier
    try:
        metadata["NODATA_VALUE"] = int(metadata["NODATA_VALUE"])
    except (ValueError, TypeError):
        print("Erreur : NODATA_VALUE doit être un nombre entier.")
        return False

    # R4 : vérifier que les valeurs sont positives
    for key in ["WIDTH", "HEIGHT", "BANDS", "PIXEL_SIZE"]:
        if metadata[key] <= 0:
            print("Erreur :", key, "doit être strictement supérieur à zéro.")
            return False

    # Vérifier le type des pixels
    datatype = str(metadata["DATATYPE"]).strip().lower()

    if datatype != "uint16":
        print("Erreur : DATATYPE doit être uint16.")
        return False

    metadata["DATATYPE"] = datatype

    return True


def validate_band_number(band_text, nb_bands):
    """Vérifie que le numéro de bande est valide."""

    try:
        band = int(band_text)
    except (ValueError, TypeError):
        print("Erreur : le numéro de bande doit être un nombre entier.")
        return False

    if band < 0 or band > nb_bands - 1:
        print("Erreur : le numéro de bande doit être entre 0 et", nb_bands - 1)
        return False

    return True