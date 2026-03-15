# Projekt: IMDb vs. Rotten Tomatoes: Der große Rating-Vergleich

## 1. Einleitung und Fragestellung
Das Ziel dieses Projekts ist der Vergleich von Filmbewertungen zwischen der Plattform IMDb (eher zuschauergetrieben) und Rotten Tomatoes (Kritiker- und Publikumsfokus). 

**Zentrale Fragestellung:** IMDb vs. Rotten Tomatoes: Der große Rating-Vergleich. (Gibt es signifikante Unterschiede zwischen den Bewertungen der beiden Plattformen? Bewerten Kritiker bestimmte Genres anders als das Publikum?)

## 2. Projektvorgaben (Checkliste FHNW)
- [x] Daten: Mindestens 2 Datenquellen (IMDb Top 1000 & Rotten Tomatoes Datensatz)
- [x] Fragen, die mit den Daten beantwortet werden sollen
- [x] Datenbereinigung
- [ ] Datentransformation
- [ ] Qualitätsprüfung
- [ ] Pipeline
- [ ] Visualisierung
- [ ] Analyse
- [ ] Protokoll / Projektbericht

## 3. Projekttagebuch & Dokumentation der Verarbeitungsschritte

### Schritt 1: Datenbeschaffung und initiales Einlesen
- **Datenquellen:** `imdb_top_1000.csv` und die entsprechenden Rotten Tomatoes Daten.
- **Aktion:** Beide Datensätze wurden in unserem Python-Skript (`import pandas as pd.py`) via `pandas` erfolgreich eingelesen.
- **Aktueller Stand:** Wir haben die relevanten Spalten wie Filmtitel (`Series_Title` / `movie_title`), Erscheinungsjahr und die Ratings (`IMDB_Rating` / `tomatometer_rating`) identifiziert.

### Schritt 2: Explorative Datenanalyse & Bereinigung
- **Erkenntnisse:**
  - **IMDb:** Enthielt 1000 Zeilen, keine fehlenden Werte, jedoch waren die Jahre (Released_Year) Strings (ein fehlerhafter Wert).
  - **Rotten Tomatoes:** Enthielt 17.712 Zeilen, 44 fehlende 	omatometer_rating und 1166 fehlende Daten (original_release_date).
- **Aktion (Datenbereinigung in data_analysis.py):**
  - IMDb: fehlerhafte Jahreszahlen per pd.to_numeric in NaN umgewandelt und gelöscht. Danach in Int-Format konvertiert (999 Zeilen verbleibend).
  - Rotten Tomatoes: Zeilen ohne 	omatometer_rating aussortiert. Aus dem originalen Startdatum wurde nur das Jahr in eine neue Spalte Released_Year_RT extrahiert (und alle ohne gültiges Jahr entfernt). Zum Schluss ins Int-Format konvertiert (16.514 Zeilen verbleibend).
- **Aktueller Stand:** Daten sind jetzt formatiert und bereit für die Verknüpfung (Datentransformation).
