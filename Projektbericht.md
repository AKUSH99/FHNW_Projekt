# Projektbericht: IMDb vs. Rotten Tomatoes – Wie Publikum und Kritiker Filme bewerten

## Zusammenfassung
Dieses Projekt geht der Frage auf den Grund, ob normale Kinogänger (IMDb) und professionelle Filmkritiker (Rotten Tomatoes) Filme unterschiedlich bewerten. Nach der Auswertung von 664 Filmen zeigt sich ein klares Bild: Kritiker vergeben extremere Noten, während das Publikum meist milder urteilt. Außerdem trennen sich die Meinungen bei neueren Filmen immer öfter. Aus diesen Erkenntnissen lassen sich smarte Strategien für das Filmmarketing ableiten.

## 1. Worum geht es?
Wer kennt es nicht: Ein Film wird von den Kritikern in der Luft zerrissen, aber das Publikum liebt ihn – oder eben umgekehrt. Plattformen wie IMDb (für das breite Publikum) und Rotten Tomatoes (oft von Fachkritikern dominiert) machen genau das sichtbar. Ziel dieser Arbeit ist es, mit echten Daten zu prüfen, ob Kritiker tatsächlich strenger oder einfach nur anders bewerten als normale Zuschauer. Und wir schauen uns an, ob sich dieser Unterschied über die Jahrzehnte hinweg verändert hat.

## 2. Wie sind wir vorgegangen?
Für die Analyse haben wir zwei große Datensätze mithilfe eines automatisierten Python-Skripts (`data_analysis.py`) untersucht. Die wichtigsten Schritte waren:

* **Aufräumen:** Zuerst wurden Tippfehler und Lücken in den Daten geschlossen. Bei der IMDb mussten beispielsweise Fehler beim Erscheinungsjahr korrigiert werden.
* **Zusammenführen:** Danach wurden beide Datensätze anhand der Filmtitel logisch verknüpft. Um Verwechslungen mit Neuverfilmungen zu verhindern, durfte das Erscheinungsjahr maximal zwei Jahre abweichen.
* **Vergleichbar machen:** Die IMDb nutzt ein System von 1 bis 10 Punkten, Rotten Tomatoes eine Prozent-Skala (bis 100). Die IMDb-Noten wurden daher einfach mit 10 multipliziert, damit man sie direkt vergleichen kann.

Am Ende blieben 664 Filme übrig, für die wir perfekte Vergleichsdaten hatten.

## 3. Was haben wir herausgefunden?

### 3.1 Kritiker nutzen die komplette Noten-Skala
Die Auswertung der Punkte-Verteilungen (`rating_density_kde.png`) zeigt deutlich: Das IMDb-Publikum ist sich oft einig und bewertet sehr viele Filme solide mit rund 80 Punkten. Richtige Verrisse sind selten. Die Kritiker auf Rotten Tomatoes sind da gnadenloser: Sie greifen bei schlechten Filmen viel härter durch, vergeben interessanterweise aber auch öfter die absolute Bestnote (nahe 100 %). Ein statistischer Test hat uns bestätigt, dass das kein Zufall ist – Kritiker legen einfach ganz andere Maßstäbe an.

### 3.2 Die "Zynismus-Lücke" bei neueren Filmen
Spannend wird es auf der Zeitachse (`rating_timeline_regression.png`). Bei älteren Filmklassikern waren sich Publikum und Kritiker meistens noch total einig. Seit den 2000er-Jahren geht die Schere aber merklich auseinander: Moderne Blockbuster, die das Publikum begeistern, fallen bei den professionellen Kritikern immer öfter durch.

### 3.3 Der "Magic Quadrant" der Filme
Um das Ganze noch greifbarer zu machen, haben wir die Filme in vier anschauliche Typen eingeteilt (`magic_quadrant_analysis.png`):
* **Die Meisterwerke:** Kritiker und Publikum sind gleichermaßen begeistert.
* **Die Kritiker-Lieblinge:** Anspruchsvolle Filme, die Experten feiern, das breite Publikum aber eher kaltlassen.
* **Das Popcorn-Kino:** Reine Unterhaltung, die das Publikum liebt, worüber die Kritiker aber nur die Nase rümpfen.
* **Die Flops:** Filme, die auf beiden Seiten komplett durchgefallen sind.

## 4. Fazit und Nutzen für die Praxis
Unsere Daten beweisen: Kritiker und normales Publikum ticken extrem unterschiedlich. Für das Marketing eines neuen Films ist diese Erkenntnis Gold wert:
* **Ist der Film typisches Popcorn-Kino**, sollte das Budget direkt in Social-Media-Kampagnen und Screenings für Fans fließen. Teure Vorführungen für die strenge Fachpresse kann man sich eher sparen, um negative Presse zu vermeiden.
* **Ist der Film ein Kritiker-Liebling**, lohnen sich exklusive Festival-Premieren und Kooperationen mit Fachmagazinen. Die guten Experten-Kritiken wirken dann als Gütesiegel, das im zweiten Schritt auch das normale Publikum ins Kino lockt.
