# Projektbericht / Protokoll: FHNW Daten-Projekt
**Thema:** IMDb vs. Rotten Tomatoes – Der große Rating-Vergleich (Zuschauer vs. Kritiker)

## 1. Einleitung und Fragestellung
Das vorliegende Daten-Projekt beschäftigt sich mit der Frage, inwiefern sich die Filmbewertungen von regulären Zuschauern (repräsentiert durch die "IMDb Top 1000") von den Einschätzungen professioneller Filmkritiker (repräsentiert durch das "Rotten Tomatoes Tomatometer") unterscheiden.
Gibt es signifikante Diskrepanzen in der Bewertung? Sind Kritiker strenger als das breite Publikum?

## 2. Datengrundlage und Methodik
Für die Analyse wurden zwei separate CSV-Datensätze herangezogen:
- `imdb_top_1000.csv` (IMDb Ratings)
- `rotten_tomatoes_movies.csv` (Rotten Tomatoes Ratings)

### 2.1 Datenbereinigung & Qualitätsprüfung (Eingehend)
Im ersten Schritt wurden die Daten eingelesen und auf fehlende Werte sowie falsche Datentypen geprüft.
- Bei den **IMDb-Daten** lagen die Veröffentlichungsjahre zum Teil in inkorrekten String-Formaten (z.B. "PG") vor. Diese wurden entfernt und in Integer umgewandelt.
- Im **Rotten Tomatoes-Datensatz** fehlten vereinzelt Ratings und Publikationsdaten. Zudem musste aus dem konkreten Datumscode (`YYYY-MM-DD`) das Jahr extrahiert werden. Datensätze ohne gültiges Rating oder Jahr wurden gelöscht.
- **Begründung der Bereinigung:** Zeilen mit fehlenden Zielvariablen (Ratings) müssen zwingend gelöscht werden, da eine Imputation (z.B. Ersetzen durch Mittelwerte) das spätere Analyseergebnis für den Vergleich verfälschen würde. Die Umwandlung der Datumsformate in konsistente Jahre (Integer) war essentiell, um sie im nächsten Schritt als Kontrollmechanismus beim Mergen nutzen zu können.

### 2.2 Datentransformation (Verknüpfung)
Um die Filmbewertungen direkt vergleichen zu können, wurden die zwei Datensätze zu einem zentralen DataFrame zusammengefasst:
1. **Normalisierung:** Alle Filmtitel wurden konsequent kleingeschrieben und unnötige Leerzeichen entfernt. 
   - *Begründung:* Unterschiedliche Schreibweisen oder Tippfehler (z.B. "The Godfather " vs "the godfather") würden einen Join verhindern.
2. **Merging / Inner Join:** Beide Tabellen wurden über den normalisierten Filmtitel verknüpft.
   - *Begründung:* Ein Inner Join stellt sicher, dass wir am Ende nur Filme betrachten, die tatsächlich auf *beiden* Plattformen bewertet wurden.
3. **Qualitätssicherung nach Join:** Um falsche Zuordnungen (z.B. bei Remakes gleichen Namens) auszufiltern, behielten wir nur Filme, deren Publikationsjahr in beiden Datensätzen um maximal 2 Jahre voneinander abweicht.
   - *Begründung:* Viele Filmtitel wie "King Kong" existieren mehrfach. Der Check des Publikationsjahres ist ein verlässlicher Filter, um Äpfel mit Äpfeln zu vergleichen.
4. **Feature Engineering:** Das IMDb-Rating (1-10) wurde rechnerisch mit 10 multipliziert (`IMDB_Rating_100`).
   - *Begründung:* Ratingskalen müssen vor einem rechnerischen oder visuellen Vergleich normiert werden, um aussagekräftige Differenzen bilden zu können.

### 2.3 Die lauffähige Pipeline
Sämtliche Schritte von lokaler Dateieinlesung, Bereinigung, Transformation bis hin zur automatischen Exportierung der Visualisierungen sind in einem zentralen Python-Skript (`data_analysis.py`) automatisiert. 
- **Begründung der Pipeline-Architektur:** Dieser Code-First-Ansatz gewährleistet eine 100%ige Reproduzierbarkeit und Fehlerfreiheit bei der Durchführung ("Single Source of Truth").

## 3. Ergebnisse und Visualisierung
Um eine ausgiebige **Qualitätsprüfung** der transformierten Zielraten vorzunehmen, wurde die Distribution statistisch überprüft (`describe()`). Das IMDb-Rating liegt im Durchschnitt bei soliden 79.3 % (da es sich primär um Top-Filme handelt). Die Rotten Tomatoes Wertung liegt im Schnitt leicht höher (88.1 %), weißt aber mit einer Standardabweichung von 10.9 (RT) gegenüber 2.8 (IMDb) eine immens höhere Varianz auf.

### 3.1 Die Visualisierungen zeigen folgendes Bild:
- **Boxplot (`rating_distribution_boxplot.png`):** Das Publikum (IMDb) bewertet die etablierten Klassiker extrem homogen – fast alle Filme liegen sehr dicht beieinander zwischen 76 % und 85 %. Bei den Kritikern (Rotten Tomatoes) ist der Wertebereich auf der Skala drastisch in die Länge gezogen. 
  - *Begründung für Boxplot:* Er eignet sich optimal, um Varianzen, Mediane und Ausreißer in direkter Gegenüberstellung zweier Metriken darzustellen.
- **Scatterplot (`rating_comparison_scatter.png`):** Das Streudiagramm illustriert sehr gut die Korrelation (bzw. deren Fehlen). Filme, die bei der IMDb-Zielgruppe eine stabile Wertung von um die 80 % genießen, fallen bei den Kritikern teils auf 100 %, teils tief unter 50 %.
  - *Begründung für Scatterplot:* Diese Darstellung mit einer perfekten Übereinstimmungslinie (x=y), deckt Divergenzen einzelner identischer Datenpunkte perfekt auf.

## 4. Fazit
Zusammenfassend lässt sich auf Grundlage der Daten festhalten, dass das breite Publikum populäre Filme deutlich "konservativer" und harmonischer bewertet. Eine Massenwertung bei IMDb gleicht sich stark an und erzeugt kaum negative Ausreißer nach unten, noch pefekte 10er-Ratings nach oben.
Professionelle Kritiker auf Rotten Tomatoes nehmen hingegen deutlich extremere Positionen ein. Sie greifen weitaus häufiger zur makellosen Höchstwertung (100%), strafen aber auch Filme, die beim Publikum eigentlich recht beliebt sind, extrem hart ab. Die Bewertung von Kritikern polarisiert demnach weitaus stärker als die des Publikums.
