#!/usr/bin/env python3

# Autoren: D1sk
# Unternehmen: T4S
# NFO-Tag-Eintrager (aus Dateinamen) v1
# Date: 20.10.2023
# Update_Date: 23.10.2023
# Zusatztool für Emby


# Bibiliotheken
import os
import re
import tkinter as tk
from tkinter import filedialog, Tk

def add_tags_as_Gruppenname_to_nfo_files(main_directory):
    # Muster, um Tags aus Dateinamen zu extrahieren 
    # (in diesem Beispiel werden Wörter nach einem Bindestrich und vor der Dateierweiterung erfasst)
    tag_pattern = r'-(.*?)(?:\..+|$)'

    # Iteriere durch alle Ordner im Hauptverzeichnis
    for root, dirs, files in os.walk(main_directory):
        for file in files:
            if file.endswith(".nfo") and file != "tvshow.nfo":
                # Wenn die Datei eine NFO-Datei ist und nicht "tvshow.nfo" heißt
                nfo_path = os.path.join(root, file)

                # Extrahiere den Tag aus dem Dateinamen
                match = re.search(tag_pattern, file)
                if match:
                    tag = match.group(1)

                    # Öffne die NFO-Datei und lese deren Inhalt
                    with open(nfo_path, "r", encoding="utf-8") as nfo_file:
                        nfo_content = nfo_file.read()

                    # Überprüfe, ob das <tag>-Element bereits im Inhalt vorhanden ist
                    if "<tag>" not in nfo_content:
                        # Suchen Sie das <runtime>-Element und fügen Sie das <tag>-Element direkt danach ein
                        nfo_content = re.sub(r'(\<runtime>[0-9]+\<\/runtime>)', f'\\1\n  <tag>{tag}</tag>', nfo_content)

                        # Schreibe den aktualisierten Inhalt zurück in die NFO-Datei
                        with open(nfo_path, "w", encoding="utf-8") as updated_nfo_file:
                            updated_nfo_file.write(nfo_content)

                        print(f"Tag '{tag}' zu NFO-Datei '{file}' hinzugefügt.")

    print("Vorgang abgeschlossen.")

#def main():
root = tk.Tk()
root.withdraw()  

# Hauptverzeichnis, das durchsucht werden soll
main_directory = filedialog.askdirectory(title='Animeordner auswählen')

add_tags_as_Gruppenname_to_nfo_files(main_directory)

#Testing
if __name__ == "__main__":
 
    main_directory = r"Path"
    add_tags_as_Gruppenname_to_nfo_files(main_directory)
    