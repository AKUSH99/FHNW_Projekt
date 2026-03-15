# Projekt: IMDb vs. Rotten Tomatoes: Der große Rating-Vergleich

## 1. Einleitung und Fragestellung
Das Ziel dieses Projekts ist der Vergleich von Filmbewertungen zwischen der Plattform IMDb (eher zuschauergetrieben) und Rotten Tomatoes (Kritiker- und Publikumsfokus). 

**Zentrale Fragestellung:** IMDb vs. Rotten Tomatoes: Der große Rating-Vergleich. (Gibt es signifikante Unterschiede zwischen den Bewertungen der beiden Plattformen? Bewerten Kritiker bestimmte Genres anders als das Publikum?)

## 2. Projektvorgaben (Checkliste FHNW)
- [x] Daten: Mindestens 2 Datenquellen (IMDb Top 1000 & Rotten Tomatoes Datensatz)
- [x] Fragen, die mit den Daten beantwortet werden sollen
- [x] Datenbereinigung
- [x] Datentransformation
- [x] Qualitätsprüfung
- [x] Pipeline
- [x] Visualisierung
- [x] Analyse
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

### Schritt 3: Datentransformation (Verknüpfung)
- **Ziel:** Beide Datensätze zu einem großen DataFrame verbinden um die Ratings vergleichen zu können.
- **Aktion (Datentransformation in data_analysis.py):**
  - Titel in beiden Datensätzen wurden in Kleinbuchstaben umgewandelt und von Leerzeichen befreit, um eine höhere Trefferquote beim Merge zu erzielen.
  - Die Tabellen wurden per *Inner Join* über den Titel (	itle_norm) zusammengefügt.
  - **Qualitätssicherung bei Verknüpfung:** Um Remakes oder Titelüberschneidungen zu vermeiden, wurden alle zusammengefügten Zeilen entfernt, bei denen die Veröffentlichungsjahre der beiden Plattformen mehr als 2 Jahre voneinander abweichen.
  - **Feature Engineering:** IMDb-Rating (1-10) wurde mit 10 multipliziert, um direkt mit dem Rotten Tomatoes Rating (1-100) vergleichbar zu sein (IMDB_Rating_100).
- **Stand:** 664 Filme konnten erfolgreich und qualitativ hochwertig gematched werden. Die Checkliste wurde aktualisiert.

### Schritt 4: Qualitätsprüfung & Visualisierung (Analyse)
- **Aktion:** Bibliotheken \matplotlib\ und \seaborn\ wurden eingebunden.
- **Qualitätsprüfung:** Mittels \describe()\ analysiert. Das IMDb-Rating liegt im Schnitt bei ~79 %, das Kritiker-Rating bei ~88 %. Die Varianzen zeigen bereits, dass Kritiker stärkere Ausschläge zulassen (besser & schlechter).
- **Visualisierungen (Pipeline-Output):**
  - **Scatterplot (\ating_comparison_scatter.png\):** Zeigt die Korrelation. Er zeigt recht deutlich, dass Rotten Tomatoes stark bei beliebten Filmen streut (viele 100%, aber zum Teil auch weit unten bei 40-50%).
  - **Boxplot (\ating_distribution_boxplot.png\):** Zeigt die Verteilungsunterschiede. Die IMDb-Werte sind sehr eng gefasst (Mitte zwischen 77 und 81), während das Tomatometer fast einen Bereich von 25 bis 100 hat.
- **Analyse-Erkenntnis:** Das Publikum bewertet die Top-Filme durchweg positiv und dicht beieinander. Kritiker der Rotten Tomatoes Plattform sind weitaus strenger und bewerten deutlich diverser, vergeben aber kurioserweise auch öfter perfekte 100%-Punktzahlen als das Publikum.

*Hiermit sind die Daten analysiert und die Vorbereitung für das Abschlussprotokoll/Projektbericht geschaffen.*

