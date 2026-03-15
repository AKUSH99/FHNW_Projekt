# Lauffähige Pipeline: FHNW Projekt

Dieses Repository enthält die vollständig automatisierte Datenpipeline (Bereinigung, Transformation, Qualitätsprüfung, Visualisierung und Analyse) zum Vergleich von IMDb- und Rotten Tomatoes-Ratings.

## Pipeline ausführen

1. **Voraussetzung:** Python muss installiert sein.
2. **Setup der Umgebung:**
   Installiere die nötigen Bibliotheken mit `pip`:
   ```bash
   pip install pandas matplotlib seaborn
   ```
   (Falls ein virtuelles Environment wie z.B. `uv` genutzt wird, wechsle in die entsprechende Umgebung).

3. **Pipeline starten:**
   Führe das Hauptskript aus:
   ```bash
   python data_analysis.py
   ```

4. **Ergebnis:**
   - Die Konsole bestätigt den Status der Bereinigung, die Transformation und die Qualitätsprüfung (statistische Kennzahlen).
   - Es werden automatisch zwei Visualisierungen generiert und im Projektordner gespeichert:
     - `rating_comparison_scatter.png`
     - `rating_distribution_boxplot.png`
