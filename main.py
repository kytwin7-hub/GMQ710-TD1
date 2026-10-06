from src.ingest import read_grid
from src.validate import validate_file_path


def main():
    path = input("Chemin du fichier .grd : ")

    if not validate_file_path(path):
        return

    lines = read_grid(path)
    print("Lignes lues :", len(lines))


main()