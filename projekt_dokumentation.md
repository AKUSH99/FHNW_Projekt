# Projekt: IMDb vs. Rotten Tomatoes: Der große Rating-Vergleich

## 1. Einleitung und Fragestellung
Das Ziel dieses Projekts ist der Vergleich von Filmbewertungen zwischen der Plattform IMDb (eher zuschauergetrieben) und Rotten Tomatoes (Kritiker- und Publikumsfokus). 

**Zentrale Fragestellung:** IMDb vs. Rotten Tomatoes: Der große Rating-Vergleich. (Gibt es signifikante Unterschiede zwischen den Bewertungen der beiden Plattformen? Bewerten Kritiker bestimmte Genres anders als das Publikum?)

## 2. Projektvorgaben (Checkliste FHNW)
- [x] Daten: Mindestens 2 Datenquellen (IMDb Top 1000 & Rotten Tomatoes Datensatz)
- [x] Fragen, die mit den Daten beantwortet werden sollen
- [ ] Datenbereinigung
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
