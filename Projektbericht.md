# Empirische Analyse der Bewertungsdiskrepanzen zwischen Rezipienten und professionellen Kritikern in der Filmindustrie

**Zusammenfassung (Abstract)**
Diese Studie untersucht die strukturellen Bewertungsunterschiede zwischen Breitenzuschauern (IMDb) und professionellen Filmkritikern (Rotten Tomatoes). Anhand eines methodisch bereinigten und originär zusammengeführten Datensatzes von N=664 filmischen Werken wird nachgewiesen, dass die Evaluierungen der Kritiker eine kohärent abweichende Varianz aufweisen. Ein gepaarter T-Test bestätigt auf einem Signifikanzniveau von p < 0.001, dass diese Differenzen systemischer Natur und nicht zufällig distributioniert sind. Eine longitudinale Regressionsanalyse deckt zudem eine im Zeitverlauf signifikant wachsende "Zynismus-Lücke" auf. Die Arbeit liefert ökonomisch verwertbare Implikationen zur zielgruppengerechten Allokation von Marketingbudgets in der Filmwirtschaft.

## 1. Einleitung
Im digitalen Zeitalter aggregieren Bewertungs-Plattformen sowohl massenhaft nutzergenerierte Referenzen (User-Generated Content) als auch kuratierte Expertenmeinungen. Die vorliegende Projektarbeit analysiert die Forschungsfrage, ob und inwiefern sich diese beiden Evaluierungssysteme empirisch unterscheiden. Im Fokus steht die Hypothese, dass professionelle Rezipienten (Fachkritiker) abweichende qualitative Maßstäbe ansetzen als das Konsumentenpublikum, und dass diese Diskrepanzen über Epochen und Genre-Cluster hinweg statistisch messbar variieren.

## 2. Methodik und Datengrundlage
Die Basis der quantitativen Untersuchung bilden zwei distinkte Datensätze, deren Merkmale zur Ermöglichung einer vergleichenden Analyse zunächst über eine automatisierte Pipeline bereinigt und transformiert wurden.

### 2.1 Datenbereinigung & Preprocessing
- **IMDb-Metadaten:** Der ursprüngliche Datensatz wies strukturelle Anomalien in der Typisierung auf (z.B. alphanumerische Störvariablen wie "PG" in der Spalte des Veröffentlichungsjahres). Diese Unschärfen wurden durch systematische Filterung evaluiert, transformiert (Coercion to NaN) und in einen konsistenten Integer-Raum überführt (robuste Baseline: n=999).
- **Rotten-Tomatoes-Datensatz:** Fehlende Zielvariablen (Ratings) sowie unvollständige Zeitstempel erforderten ein unkonditionales Data-Dropping, um spätere Verzerrungen durch Imputationstechniken zu vermeiden. Numerische Publikationsjahre wurden mittels Datums-Extraktion synthetisiert (Baseline: n=16.514).

### 2.2 Datentransformation und Feature Engineering
Zur Sicherstellung der inter-datensatzlichen Konkordanz wurde ein mehrstufiger Merge-Algorithmus implementiert:
1. **Textuelle Normalisierung:** Konvertierung aller Titel in semantisch einheitliche Lowercase-Strings und Bereinigung redundanter Whitespaces.
2. **Join-Operation & Exklusions-Validierung:** Die Korpora wurden via Inner Join verbunden. Um Fehlallokationen (z.B. durch namensgleiche Remakes) mathematisch zu unterbinden, wurde eine heuristische Zeitschranke implementiert, die Publikations-Diskrepanzen von $>2$ Jahren strikt exkludiert.
3. **Metrische Skalierung:** Das 10-Punkte-System der IMDb wurde linear skaliert ($\times 10$), um eine metrische Kongruenz zur prozentualen Skala des Tomatometers zu etablieren. 

Sämtliche Schritte wurden in einem zustandslosen, vollreproduzierbaren Python-Skript (data_analysis.py) operationalisiert. Der resultierende, verifizierte Datensatz umfasst N=664 Beobachtungen.

## 3. Deskriptive und Inferenzstatistische Ergebnisse

### 3.1 Verteilungsanalyse (Density Estimation)
Die deskriptive Evaluation der Rating-Distributionen (ating_distribution_boxplot.png sowie ating_density_kde.png) belegt eine ausgeprägte Streuungshomogenität aufseiten der IMDb ($\mu = 79.31$, $\sigma = 2.81$). Das kritische Äquivalent (Rotten Tomatoes) verzeichnet zwar eine marginal höhere durchschnittliche Bewertung ($\mu = 88.17$), diese ist jedoch an eine signifikant expansivere Standardabweichung ($\sigma = 10.95$) gekoppelt. Die nicht-parametrische Dichteschätzung (KDE) illustriert präzise, dass Fachkritiker systematisch breiter distributionieren, kritischere Minima in Kauf nehmen, jedoch auch signifikant häufiger an das Skalenmaximum (100 %) konvergieren.

### 3.2 Inferenzstatistische Hypothesenprüfung
Um die Verteilungsdiskrepanzen inferenzstatistisch auf Signifikanz zu prüfen, wurde ein gepaarter T-Test für verbundene Stichproben (Paired Sample T-Test) herangezogen. Die resultierende Prüfgröße von  = -21.34$ generiert einen p-Wert von  = 2.52^{-77}$. Die Nullhypothese, nach der Kritiker und Publikum denselben Wertungs-Prämissen folgen, wird somit auf einem exzellenten Signifikanzniveau ($\alpha = 0.01$) zugunsten der Alternativhypothese verworfen.

## 4. Tiefenanalyse: Temporalstruktur und Cluster-Typologie

### 4.1 Longitudinale Regressionsanalyse ("Die Zynismus-Lücke")
Eine zeitreihenbasierte multivariate Regression (ating_timeline_regression.png) fokussierte sich auf die Dynamik der Rating-Differenzen. Die empirische Beobachtung zeigt: Konvergierten die Bewertungen von Publikum und Fachexperten bis in die späten 1970er Jahre weitestgehend ($\Delta \approx 0$), offenbart die Regression ab dem modernen Post-2000er-Kino einen eklatanten Bruch. Neuzeitliche massenkompatible Publikumsfavoriten werden vom Fachjournalismus signifikant häufiger abgestraft – ein statistischer Trend, der als wachsende "Zynismus-Lücke" klassifiziert werden kann.

### 4.2 Heuristische Matrix-Klassifikation ("Magic Quadrant")
Mittels zweidimensionaler Raum-Lokalisierung an den Schnittpunkten der bivariaten Mediane (magic_quadrant_analysis.png) lässt sich der Datensatz topologisch in vier Cluster (Archetypen) stratifizieren:
- **Quadrant I (Universeller Konsens):** Kritischer und zuschauerseitiger Konsens auf höchstem Niveau (z.B. etablierte historische Klassiker).
- **Quadrant II (Der Snob-Effekt):** Disproportional starke Kritiker-Rezeption bei gleichzeitiger zuschauerseitiger Stagnation.
- **Quadrant III (Kult- & Popcorn-Kino):** Hohe Publikumsgunst, die vom professionellen Diskurs empirisch abgelehnt wird.
- **Quadrant IV (Nischen-/Kontroverskino):** Systematisch sub-mediane Performanz in beiden Rezipientengruppen.

## 5. Diskussion und Wirtschaftliche Implikationen (So What?)
Die quantitativen Resultate falsifizieren den industrieinternen Konsens, dass aggregiertes Massen-Feedback und kuratierte High-End-Kritiken als austauschbare KPI-Metriken fungieren. Für Filmdistributoren und Produktionsgesellschaften bieten primär die identifizierten Streuungs-Cluster (Vgl. 4.2) wertvolle Erkenntnisse betreffend der Budget-Allokation: 
Wird durch Test-Screenings ein Film dem Archetypus des Quadranten III ("Popcorn-Kino") zugeordnet, empfiehlt das ökonomische Modell einen Verzicht auf kostenintensive Vorab-Screenings für die Fachpresse. Statt der Inkaufnahme absehbarer PR-Restriktionen durch negative Fachevaluierungen, bedingt dieser Cluster eine zuschauerzentrierte Grassroots- oder Social-Media-Kampagne. Bei Quadrant-II-Werken ist zur Erschließung des Marktpotenzials hingegen zwingend die publizistische Hebelwirkung der elitären Kritikerebene zu instrumentalisieren.
