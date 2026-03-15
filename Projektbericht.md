# Projektbericht: IMDb vs. Rotten Tomatoes – Eine vergleichende Analyse von Publikums- und Kritikerbewertungen

## Management Summary
Im Rahmen dieser Projektarbeit wurde das Bewertungsverhalten von regulären Kinobesuchern und hochspezialisierten Filmkritikern empirisch untersucht. Grundlage der Analyse bilden die öffentlich zugänglichen Filmdatenbanken IMDb (breites Publikum) und Rotten Tomatoes (Fachpresse). Nach einer umfassenden Datenbereinigung und Zusammenführung beider Datensätze verblieb ein finales Sample von 664 Filmen. Die Auswertung zeigt statistisch signifikante Unterschiede: Kritiker schöpfen das Bewertungsspektrum deutlich stärker aus, strafen schlechte Filme konsequenter ab und vergeben gleichzeitig häufiger Höchstwertungen. Darüber hinaus lässt sich eine über die Jahrzehnte wachsende Diskrepanz ("Zynismus-Lücke") feststellen. Die Arbeit schließt mit konkreten Handlungsempfehlungen für das strategische Filmmarketing ab.

## 1. Einleitung und Ausgangslage
In der heutigen Unterhaltungsindustrie spielen Online-Bewertungen eine zentrale Rolle. Sie beeinflussen nicht nur die Entscheidungen von Millionen von Kinogängern, sondern entscheiden oft auch über den wirtschaftlichen Erfolg oder Misserfolg einer Produktion. Dabei stehen sich zwei entscheidende Bewertungssysteme gegenüber: Die massenhaften Zuschauerwertungen auf Plattformen wie der IMDb und die aggregierten Expertenmeinungen auf Rotten Tomatoes.

In der Filmwelt existiert das hartnäckige Klischee, dass Filmkritiker und das reguläre Publikum bei der Bewertung von Filmen völlig unterschiedliche Maßstäbe anlegen. Während Zuschauer oft einen hohen Unterhaltungswert und emotionale Bindung honorieren, achten Kritiker stärker auf narrative Komplexität, Innovation und handwerkliche Umsetzung. Ziel dieser Arbeit ist es, diese Vermutung anhand von Echtdaten quantitativ zu überprüfen. Dabei sollen insbesondere die Fragen beantwortet werden, wie stark sich die Bewertungen unterscheiden, ob sich dieser Unterschied historisch verändert hat und welche Cluster sich dabei identifizieren lassen.

## 2. Datengrundlage und Methodik
Um aussagekräftige Ergebnisse zu erzielen, wurden zwei verschiedene Datensätze verarbeitet. Die Umsetzung erfolgte vollständig automatisiert in einer Python-Umgebung.

### 2.1 Datenbereinigung und Transformation
Im ersten Schritt wurden die Rohdaten strukturiert bereinigt. Der IMDb-Datensatz erforderte Korrekturen bei der Datentypisierung, da beispielsweise das Erscheinungsjahr teilweise fehlerhafte Zeichen enthielt. Fehlende oder ungültige Werte wurden systematisch entfernt, um Verzerrungen zu vermeiden. Beim Datensatz von Rotten Tomatoes wurden Datumsangaben standardisiert und das Publikationsjahr extrahiert.

### 2.2 Zusammenführung der Daten (Merge)
Damit die Bewertungen direkt miteinander verglichen werden können, wurden die Datensätze über einen "Inner Join" anhand der Filmtitel verknüpft. Um eine fälschliche Zuordnung von namensgleichen Filmen (etwa bei Remakes wie "King Kong") zu verhindern, wurde eine Validierungsregel implementiert: Nur Filme, deren Erscheinungsjahr in beiden Datensätzen maximal zwei Jahre voneinander abweicht, wurden in den finalen Datensatz übernommen.

### 2.3 Skalierung und Vergleichbarkeit
Ein methodisches Problem stellte die unterschiedliche Skalierung der Bewertungen dar. Während die IMDb ein 10-Punkte-System verwendet, operiert Rotten Tomatoes mit einem prozentualen Tomatometer (0 bis 100 %). Um eine direkte, numerische Vergleichbarkeit zu gewährleisten, wurden die IMDb-Werte linear mit dem Faktor 10 multipliziert. Der finale Datensatz nach der Bereinigung umfasst N = 664 überprüfte Filme.

## 3. Ergebnisse der explorativen Datenanalyse

### 3.1 Bewertungsunterschiede und Streuung
Die Analyse der Punkteverteilung (`rating_density_kde.png`) zeigt aufschlussreiche Muster. Das IMDb-Publikum bewertet Filme insgesamt relativ moderat und homogen; die meisten Wertungen durch die Masse konzentrieren sich im Bereich von 75 bis 85 Punkten. Extreme Verrisse sind selten. Die Kritiker auf Rotten Tomatoes reagieren hingegen wesentlich extremer: Ihre Noten streuen deutlich breiter. Sie vergeben häufiger sehr niedrige Bewertungen, belohnen aber herausragende Filme auch extrem oft mit der absoluten Höchstwertung (nahe 100 %). Ein durchgeführter statistischer T-Test bestätigt anschaulich, dass diese Bewertungsunterschiede signifikant sind und nicht auf Zufall beruhen.

### 3.2 Zeitliche Entwicklung ("Zynismus-Lücke")
Besonders interessant ist die Betrachtung der Bewertungen im historischen Verlauf (`rating_timeline_regression.png`). Die Regressionsanalyse zeigt, dass sich Kritiker und Publikum bei Filmen aus dem 20. Jahrhundert (etwa bis zu den 1980er Jahren) weitestgehend einig waren. Ab den 2000er Jahren öffnet sich die Schere jedoch merklich: Moderne Publikumsfilme werden von der Fachpresse heutzutage zunehmend kritischer bewertet als früher. Dieser Trend wurde im Rahmen des Projekts als wachsende "Zynismus-Lücke" identifiziert.

### 3.3 Der "Magic Quadrant" der Filme
Zur besseren Typisierung wurden die Filme in einem Streudiagramm (`magic_quadrant_analysis.png`) der jeweiligen Durchschnittswertungen gegenübergestellt und in vier Kernkategorien unterteilt:
* **Meisterwerke:** Filme, die sowohl von der breiten Masse als auch von den Fachkritikern außerordentlich hoch bewertet werden (z. B. etablierte Filmklassiker).
* **Kritiker-Lieblinge:** Oftmals Arthouse- oder Independentfilme. Sie werden von der Fachwelt für ihre Innovation gefeiert, stoßen beim Mainstream-Publikum aber auf weniger Gegenliebe.
* **Popcorn-Kino:** Typische Blockbuster oder Actionfilme, die genau den Nerv der Zuschauer treffen, filmhistorisch oder handwerklich von den Kritikern jedoch abgestraft werden.
* **Misserfolge:** Filme, die auf ganzer Linie enttäuschen und niemanden ansatzweise überzeugen konnten.

## 4. Reflexion und Limitationen
Bei der Betrachtung der Ergebnisse muss berücksichtigt werden, dass es sich beim Ausgangsdatensatz primär um die Top-Filme der IMDb handelt. Filme mit durchgehend sehr mäßigen Bewertungen sind im Datensatz leicht unterrepräsentiert, was zu einem sogenannten Selection Bias (Auswahlverzerrung) führen könnte. Für eine noch belastbarere Aussagekraft sollten in Zukunft völlig zufällig gezogene Filmdatensätze hinzugezogen werden. Dennoch liefern die vorliegenden Daten einen robusten Einblick in das generelle Bewertungsverhalten der beiden Lager.

## 5. Fazit und Handlungsempfehlungen
Die durchgeführte Analyse belegt eindrücklich, dass das Massenpublikum und professionelle Filmkritiker grundlegend verschiedene Anforderungen an filmische Werke stellen. Für Filmstudios und Distributoren ergeben sich daraus direkt anwendbare Marketing-Strategien:
* **Zielgruppenfokussiertes Marketing:** Zeigen erste Testvorführungen, dass ein Film in die Kategorie "Popcorn-Kino" fällt, sollte das Marketingbudget primär in Direct-to-Consumer-Kanäle (z. B. Social Media) investiert werden. Kostspielige Pressevorführungen bergen hier eher das Risiko von negativer Berichterstattung und sollten gemieden werden.
* **Nutzung von Experten-Meinungen:** Fällt ein Film eher in das Segment "Kritiker-Liebling", ist eine gezielte Einreichung bei Filmfestivals ratsam. Die daraus resultierenden positiven Fachkritiken fungieren als inhaltlicher Qualitätsgarant und können genutzt werden, um anschließend auch das Interesse eines breiteren Publikums zu wecken.
