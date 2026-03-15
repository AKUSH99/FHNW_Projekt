# Projektbericht: IMDb vs. Rotten Tomatoes – Ein Vergleich von Publikums- und Kritikerbewertungen

## Management Abstract
In dieser Projektarbeit wurde untersucht, wie sich die Filmbewertungen der breiten Masse (Zuschauer auf IMDb) von denen professioneller Filmkritiker (Rotten Tomatoes) unterscheiden. Nach der Zusammenführung und sorgfältigen Bereinigung der Datensätze zeigte die Analyse von 664 Filmen signifikante Unterschiede: Kritiker bewerten im Durchschnitt extremer (sowohl positiver als auch negativer) als das Publikum. Zudem zeigt sich über die Jahrzehnte eine wachsende "Zynismus-Lücke" – moderne Filme spalten Publikum und Kritiker zunehmend. Aus diesen Erkenntnissen lassen sich konkrete Marketing-Strategien für die Filmindustrie ableiten.

## 1. Einleitung und Zielsetzung
Dank Plattformen wie IMDb und Rotten Tomatoes stehen uns heute Millionen von Nutzerbewertungen sowie Einschätzungen von professionellen Kritikern zur Verfügung. Oft entsteht der Eindruck, dass Kritiker Filme anders wahrnehmen als das normale Kinopublikum. Ziel dieser Arbeit ist es, diese Vermutung anhand von Echtdaten empirisch zu überprüfen. Wir untersuchen, ob es messbare Abweichungen gibt und wie sich das Verhältnis zwischen Zuschauern und Experten im Laufe der Zeit entwickelt hat.

## 2. Datengrundlage und Methodik
Für die Analyse wurden zwei separate Datensätze verwendet und in einem Python-Skript (data_analysis.py) automatisiert verarbeitet:

* **Datenbereinigung:** Zunächst wurden fehlende oder ungültige Werte entfernt und Datentypen standardisiert. Bei der IMDb mussten beispielsweise Buchstabendreher oder falsche Kürzel beim Erscheinungsjahr bereinigt werden, während bei Rotten Tomatoes Datumsangaben in ein einheitliches Format überführt wurden.
* **Zusammenführung (Merge):** Die beiden Datensätze wurden basierend auf dem Filmtitel verknüpft. Um Fehler durch Remakes mit dem gleichen Titel zu vermeiden, wurden nur Filme zusammengeführt, deren Erscheinungsjahr maximal zwei Jahre voneinander abweicht.
* **Vergleichbarkeit:** Das 10-Punkte-System der IMDb wurde mit 10 multipliziert, um es mit der 100-Prozent-Skala von Rotten Tomatoes ('Tomatometer') direkt vergleichen zu können.

Nach der Bereinigung verblieben 664 Filme, die in beiden Datensätzen vollständig dokumentiert waren.

## 3. Ergebnisse der Analyse

### 3.1 Bewertungsverhalten im Vergleich
Die Analyse der Punkte-Verteilungen (ating_density_kde.png) zeigt ein klares Bild: Das IMDb-Publikum bewertet Filme sehr homogen; die meisten Wertungen bewegen sich im Bereich um die 80 Punkte. Die Kritiker auf Rotten Tomatoes nutzen die Bewertungsspanne hingegen wesentlich stärker aus: Sie strafen durchgefallene Filme härter ab, vergeben aber auch deutlich öfter echte Spitzenwertungen (nahe 100%). Ein statistischer T-Test bestätigt anschaulich, dass die Unterschiede nicht zufällig sind, sondern eine grundlegend andere Bewertungslogik der Kritiker dahintersteckt ( < 0.001$).

### 3.2 Die "Zynismus-Lücke" im Zeitverlauf
Ein Blick auf die zeitliche Entwicklung (ating_timeline_regression.png) deckte eine interessante Dynamik auf. Während historische Filmklassiker von Zuschauern und Kritikern oft noch ähnlich hoch bewertet wurden, geht die Schere ab dem Kino der 2000er-Jahre immer weiter auseinander. Moderne Blockbuster, die beim Publikum gut ankommen, fallen bei der Fachpresse immer häufiger durch. 

### 3.3 Der "Magic Quadrant" der Filmindustrie
Um die Filme besser kategorisieren zu können, wurden sie im sogenannten "Magic Quadrant" plottiert (magic_quadrant_analysis.png), abgeleitet aus den jeweiligen Durchschnittswertungen:
* **Klassiker / Meisterwerke:** Filmkunst, bei der sich Kritiker und Publikum einig sind (hohe Wertungen auf beiden Seiten).
* **Kritiker-Lieblinge:** Filme mit hohem Anspruch, die von der Fachpresse gefeiert werden, aber das Massenpublikum eher überfordern oder langweilen.
* **Popcorn-Kino:** Unterhaltung pur – das Publikum liebt den Film, die Kritiker vergeben jedoch schlechte Noten.
* **Flops / Nischenfilme:** Filme, die weder die Experten noch die breite Masse überzeugen konnten.

## 4. Fazit und Nutzen für die Praxis
Die Resultate beweisen, dass Kritiker- und Zuschauerwertungen zwei völlig unterschiedliche Zielgruppen und Massstäbe abbilden. Diese Erkenntnis hat direkten Nutzen für das Filmmarketing:
* **Bei "Popcorn-Kino":** Wenn Test-Screenings zeigen, dass ein Film dem Publikum extrem gefällt, der anspruchsvollen Fachpresse aber wohl missfällt, sollte das Marketingbudget primär in Social Media und Fan-Kampagnen fliessen. Teure Fachpresse-Screenings sollten gemieden werden, um schlechte PR zu umgehen.
* **Bei "Kritiker-Lieblingen":** Hier ist eine clevere Presse-Strategie entscheidend. Exklusive Vorführungen auf Festivals und starke Reviews in Zeitschriften können dem Film das nötige Prestige verleihen, um anschliessend als "Muss-man-gesehen-haben"-Titel das Interesse des normalen Publikums zu wecken.
