import csv
from pathlib import Path

dossier = Path(input("Dossier à scanner : "))

with open("inventaire.csv", "w", newline="", encoding="utf-8") as f:
    ecrivain = csv.writer(f)
    ecrivain.writerow(["Nom", "Taille (Go)"])

    for fichier in dossier.iterdir():
        if fichier.is_file():
            taille_go = fichier.stat().st_size / (1024 * 1024 * 1024)
            ecrivain.writerow([fichier.name, round(taille_go, 1)])


