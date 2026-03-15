# Projektbericht / Protokoll: FHNW Daten-Projekt
**Thema:** IMDb vs. Rotten Tomatoes – Der große Rating-Vergleich (Zuschauer vs. Kritiker)

## 1. Einleitung und Fragestellung
Das vorliegende Daten-Projekt beschäftigt sich mit der Frage, inwiefern sich die Filmbewertungen von regulären Zuschauern (repräsentiert durch die "IMDb Top 1000") von den Einschätzungen professioneller Filmkritiker (repräsentiert durch das "Rotten Tomatoes Tomatometer") unterscheiden.
Gibt es signifikante Diskrepanzen in der Bewertung? Sind Kritiker strenger als das breite Publikum?

## 2. Datengrundlage und Methodik
Für die Analyse wurden zwei separate CSV-Datensätze herangezogen:
- `imdb_top_1000.csv` (IMDb Ratings)
- `rotten_tomatoes_movies.csv` (Rotten Tomatoes Ratings)

### 2.1 Datenbereinigung
Im ersten Schritt wurden die Daten eingelesen und auf fehlende Werte sowie falsche Datentypen geprüft:
- Bei den **IMDb-Daten** lagen die Veröffentlichungsjahre zum Teil in inkorrekten String-Formaten (z.B. "PG") vor. Diese wurden entfernt und fehlerfrei in Integer umgewandelt (resultierend in 999 nutzbaren Datensätzen).
- Im **Rotten Tomatoes-Datensatz** fehlten vereinzelt Ratings und Publikationsdaten. Zudem musste aus dem konkreten Datumscode (`YYYY-MM-DD`) das Jahr extrahiert werden. Datensätze ohne Rating wurden gelöscht (resultierend in 16.514 nutzbaren Datensätzen).

### 2.2 Datentransformation (Verknüpfung)
Um die Filmbewertungen direkt vergleichen zu können, wurden die zwei Datensätze zu einem zentralen DataFrame zusammengefasst:
1. **Normalisierung:** Alle Filmtitel wurden konsequent kleingeschrieben und unnötige Leerzeichen entfernt.
2. **Merging / Inner Join:** Beide Tabellen wurden über den normalisierten Filmtitel verknüpft.
3. **Qualitätssicherung:** Um falsche Zuordnungen (z.B. bei Remakes gleichen Namens) auszufiltern, behielten wir nur Filme, deren Publikationsjahr in beiden Datensätzen um maximal 2 Jahre voneinander abweicht.
4. **Feature Engineering:** Das IMDb-Rating (1-10) wurde rechnerisch mit 10 multipliziert (`IMDB_Rating_100`), um eine einheitliche 100-Punkte-Skala für den direkten Vergleich mit Rotten Tomatoes zu schaffen.

Das Endresultat der Transformation ist ein hochqualitativer, zusammengeführter Datensatz mit **664 Filmen**.

## 3. Ergebnisse und Visualisierung
Bereits die statistische Evaluierung zeigte deutliche Muster: Das IMDb-Rating liegt im Durchschnitt bei soliden 79.3 % (da es sich primär um Top-Filme handelt). Die Rotten Tomatoes Wertung liegt im Schnitt leicht höher (88.1 %), weißt aber mit einer Standardabweichung von 10.9 (RT) gegenüber 2.8 (IMDb) eine immens höhere Varianz auf.

### 3.1 Die Visualisierungen zeigen folgendes Bild:
- **Boxplot (`rating_distribution_boxplot.png`):** Das Publikum (IMDb) bewertet die etablierten Klassiker extrem homogen – fast alle Filme liegen sehr dicht beieinander zwischen 76 % und 85 %. Bei den Kritikern (Rotten Tomatoes) ist der Wertebereich auf der Skala drastisch in die Länge gezogen. Das Spektrum reicht regulär tief bis auf 60 % und in den Extremen sogar bis auf die 20 %.
- **Scatterplot (`rating_comparison_scatter.png`):** Das Streudiagramm illustriert sehr gut die geringe Korrelation der Ausschläge. Filme, die bei der IMDb-Zielgruppe eine stabile "Lieblingsfilm-Wertung" von um die 80 % genießen, fallen bei den Kritikern entweder auf perfekte 100 % (sehr häufig) oder sie stürzen mit Kritiker-Verrissen auf unter 50 % ab.

## 4. Fazit
Zusammenfassend lässt sich auf Grundlage der Daten festhalten, dass das breite Publikum populäre Filme deutlich "konservativer" und harmonischer bewertet. Eine Massenwertung bei IMDb gleicht sich stark an und erzeugt kaum negative Ausreißer nach unten, noch pefekte 10er-Ratings nach oben.
Professionelle Kritiker auf Rotten Tomatoes nehmen hingegen deutlich extremere Positionen ein. Sie greifen weitaus häufiger zur makellosen Höchstwertung (100%), strafen aber auch Filme, die beim Publikum eigentlich recht beliebt sind, extrem hart ab. Die Bewertung von Kritikern polarisiert demnach weitaus stärker als die des Publikums.
