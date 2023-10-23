# NFO-Tag-Eintrager (aus Dateinamen)

![GitHub](https://img.shields.io/badge/python-3.x-blue.svg)
![GitHub](https://img.shields.io/badge/license-MIT-green)

**NFO-Tag-Eintrager** ist ein einfaches Python-Tool, das entwickelt wurde, um NFO-Dateien von Emby in einem Verzeichnisbaum zu durchsuchen und NFO-Tags aus Dateinamen zu extrahieren. Dieses Tool ist besonders hilfreich, wenn du Anime-Serien die mit dem Gruppname gettagt sind in deinen NFO-Dateien speichern möchtest damit sie auf Emby angezeigt werden.


## Features

- **Einfache Bedienung**: Das Tool verwendet die tkinter-Bibliothek, um das Hauptverzeichnis auszuwählen, in dem nach NFO-Dateien gesucht werden soll.

- **Extrahiere Tags**: Das Tool extrahiert Tags aus Dateinamen, die nach einem Bindestrich und vor der Dateierweiterung auftreten. Diese Tags werden dann in den zugehörigen NFO-Dateien als `<tag>`-Elemente gespeichert.

- **Intelligente Aktualisierung**: Wenn das `<tag>`-Element bereits in der NFO-Datei vorhanden ist, wird das Tool die Datei überspringen. Es aktualisiert nur NFO-Dateien, die den gewünschten Tag noch nicht enthalten.

## Installation

1. **Voraussetzungen**: Stelle sicher, dass Python 3.x auf deinem System installiert ist.

2. **Abhängigkeiten installieren**: Führe `pip install tkinter` aus, um die erforderliche `tkinter`-Bibliothek zu installieren.

3. **Repositorium klonen**: Klone dieses Repositorium oder lade es als ZIP-Datei herunter und entpacke es.

## Anwendung

1. **Ausführung**: Führe die Datei `NFO-Tag-Eintrager.py` aus.

2. **Hauptverzeichnis auswählen**: Verwende das angezeigte Datei-Dialogfeld, um das Hauptverzeichnis auszuwählen, das durchsucht werden soll.

3. **Starte den Vorgang**: Klicke auf die Schaltfläche, um den Vorgang zu starten.

4. **Überwachung des Fortschritts**: Das Tool wird alle NFO-Dateien im ausgewählten Verzeichnisbaum durchsuchen und die Tags in den NFO-Dateien aktualisieren.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Weitere Informationen findest du in der [LICENSE](LICENSE)-Datei.

**Hinweis**: Dieses Tool wurde von D1sk entwickelt und wird auf freiwilliger Basis bereitgestellt. Bei Fragen oder Anliegen kannst du mich gerne kontaktieren.


