def validate_file_path(path):
    """Vérifie que le fichier existe et qu'il peut être ouvert."""
    try:
        with open(path, "rb"):
            pass
    except OSError:
        print("Erreur : impossible d'ouvrir le fichier :", path)
        return False

    return True