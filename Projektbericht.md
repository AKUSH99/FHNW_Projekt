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
- **KDE Plot / Dichteverteilung (`rating_density_kde.png`):** Eine anspruchsvolle Kernel-Density-Estimation (KDE) veranschaulicht die glatte Verteilungsfunktion beider Ratings ohne die künstlichen Bins eines Histogramms.

## 4. Statistische Signifikanzprüfung & Erweiterte Analyse
Um über ein rein visuelles "Deskriptiv"-Niveau hinauszugehen, wurde ein **gepaarter T-Test** (mittels `SciPy`) über die verbundenen Stichproben der beiden Datensätze durchgeführt.
- **Ergebnis des T-Tests:** Die T-Statistik liegt bei -21.34 und der p-Wert bei $2.52^{-77}$. Da der p-Wert extrem nah an 0 ist, konnten wir die *Nullhypothese* (dass die Raten beider Gruppen systematisch identisch sind) verwerfen. Die Diskrepanz ist statistisch hoch signifikant!
- **Genre-Cluster-Analyse:** Eine eigens entwickelte Lambda-Split-Logik zum Isolieren der Hauptgenres zeigte zudem auf, woher diese Unterschiede kommen: Während sich Kritiker und Publikum bei *Action* und *Mystery* meistens sehr ähnlich sind, gibt es bei *Comedy* (Durchschnittlich über 10 Punkte Abweichung) und *Animation* gravierende Meinungsverschiedenheiten.

## 5. Tiefenanalyse & Wirtschaftliche Implikationen (Business Insights)
Das reine Feststellen von Diskrepanzen greift für eine vollumfängliche Analyse zu kurz. Um den Datensatz voll auszuschöpfen, wurden im Rahmen der Tiefenanalyse methodisch komplexe Visualisierungen entwickelt, um *Trends* sowie *Archetypen* von Filmen zu isolieren:

### 5.1 Zeitreihen-Analyse: Die wachsende "Zynismus-Lücke"
Mittels einer multivariaten Regression (`rating_timeline_regression.png`) wurde die Rating-Differenz über die Produktionsjahre (Epochen) hinweg geplottet. 
- **Erkenntnis:** Bei Filmen zwischen 1930 und 1970 liegen Kritiker und Publikum meistens auf einer Wellenlänge (Differenz pendelt nahe der Null-Linie). Je moderner ein Film jedoch ist (ab ca. Jg 2000), desto aggressiver spaltet sich die Meinung auf: Publikums-Lieblinge werden heute viel gezielter von der Fachpresse abgestraft – eine wachsende "Zynismus-Lücke".

### 5.2 Der "Magic Quadrant" der Filmbewertungen
Ähnlich wie in strategischen Management-Frameworks haben wir einen Scatterplot (`magic_quadrant_analysis.png`) in vier Quadranten unterteilt, zentriert auf den Median beider Bewertungs-Systeme. Dies deckt vier messbare Film-Archetypen auf:
- **Quadrant 1 (Top Rechts - Meisterwerke):** Filme, welche universell von beiden Lagern genossen werden (z.B. *The Godfather*). Ein sicheres Investment.
- **Quadrant 2 (Top Links - Kritiker-Lieblinge / Snob-Effekt):** Streng journalistisch gelobt, oft aber zu komplex / nischig für das Massenpublikum.
- **Quadrant 3 (Unten Rechts - Popcorn-Kino):** Filme, welche beim Zielpublikum massiv einschlagen, für Kritiker aber "zu stumpf" sind. 

### 5.3 Handlungsempfehlung ("So What?")
Für ein Filmstudio haben diese Analysen harte Implikationen für Marketing-Entscheidungen. Wenn Test-Agencies ein Action-Movie im Format des "Popcorn-Kinos" (Quadrant 3) einordnen, sollte ein Studio darauf verzichten, das Werbebudget in Presse-Screenings und Kritiker-Reviews zu stecken (potenzielle negative PR-Schäden). Stattdessen lohnt sich ein voll auf den Endkonsumenten fokussiertes Grassroots-/Social-Media-Marketing. Solche Erkenntnisse machen die Diskrepanz wirtschaftlich direkt greif- und nutzbar.

## 6. Fazit
Zusammenfassend lässt sich auf Grundlage der Signifikanzprüfung festhalten, dass das breite Publikum populäre Filme deutlich "konservativer" und harmonischer bewertet. Eine Massenwertung bei IMDb gleicht sich stark an und erzeugt kaum negative Ausreißer nach unten, noch pefekte 10er-Ratings nach oben. Die erweitere Trend- und Quadranten-Analyse zeigt aber, dass dies kein reiner Zufall ist, sondern stark an Genres gebunden ist und dieser Riss sich zeitgeschichtlich massiv verstärkt.
Professionelle Kritiker auf Rotten Tomatoes nehmen hingegen deutlich extremere Positionen ein. Sie greifen weitaus häufiger zur makellosen Höchstwertung (100%), strafen aber auch Filme, die beim Publikum eigentlich recht beliebt sind, extrem hart ab. Die Bewertung von Kritikern polarisiert demnach weitaus stärker als die des Publikums.
