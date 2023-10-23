#!/usr/bin/env python3

# Autoren: D1sk
# Unternehmen: T4S
# NFO-Tag-Eintrager (aus Dateinamen) v1
# Date: 20.10.2023
# Update_Date: 23.10.2023
# Zusatztool für Emby

# Bibliotheken
import os
import re
import tkinter as tk
from tkinter import filedialog, Tk

def add_tags_as_Gruppenname_to_nfo_files(main_directory):
    # Dieses Muster erfasst den Text nach dem letzten Bindestrich bis zum Dateiende.
    # Es sucht nach einem Bindestrich, gefolgt von Zeichen (einschließlich Punkt), bis zum Dateiende.
    tag_pattern = r'-(\w+)(?:\.\w+)?$'

    # Iteriere durch alle Ordner im Hauptverzeichnis
    for root, dirs, files in os.walk(main_directory):
        for file in files:
            if file.endswith(".nfo") and file != "tvshow.nfo":
                # Wenn die Datei eine NFO-Datei ist und nicht "tvshow.nfo" heißt
                nfo_path = os.path.join(root, file)

                # Nur den Dateinamen ohne Pfad und Erweiterung extrahieren
                file_name = file.split("/")[-1].split(".nfo")[0]
                # Extrahiere den Tag aus dem Dateinamen
                match = re.search(tag_pattern, file_name)
                if match:
                    tag = match.group(1)

                    # Öffne die NFO-Datei und lese deren Inhalt
                    with open(nfo_path, "rb") as nfo_file:
                        nfo_content = nfo_file.read()

                    # Überprüfe, ob das <tag>-Element bereits im Inhalt vorhanden ist
                    # Überprüfe, ob das "<tag>"-Element bereits im Inhalt vorhanden ist (als Bytes)
                    if b"<tag>" not in nfo_content:
                        # Suchen Sie das <runtime>-Element und fügen Sie das <tag>-Element direkt danach ein (als Bytes)
                        nfo_content = re.sub(b'(\<runtime>[0-9]+\<\/runtime>)', f'\\1\n  <tag>{tag}</tag>'.encode(), nfo_content)

                    # Schreibe den aktualisierten Inhalt zurück in die NFO-Datei
                    with open(nfo_path, "wb") as updated_nfo_file:
                        updated_nfo_file.write(nfo_content)

                        print(f"Tag '{tag}' zu NFO-Datei '{file}' hinzugefügt.")

    print("Vorgang abgeschlossen.")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  

    # Hauptverzeichnis, das durchsucht werden soll
    main_directory = filedialog.askdirectory(title='Animeordner auswählen')
    add_tags_as_Gruppenname_to_nfo_files(main_directory)
