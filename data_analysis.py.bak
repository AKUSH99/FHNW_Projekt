import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. DATEN EINLESEN (Data Ingestion)
# ==========================================

# Lade den IMDb Datensatz (Das Publikum)
# Wir laden direkt nur die Spalten, die wir wirklich brauchen
imdb_cols =['Series_Title', 'Released_Year', 'Genre', 'IMDB_Rating']
df_imdb = pd.read_csv('imdb_top_1000.csv', usecols=imdb_cols)

# Lade den Rotten Tomatoes Datensatz (Die Kritiker)
rt_cols = ['movie_title', 'original_release_date', 'tomatometer_rating']
df_rt = pd.read_csv('rotten_tomatoes_movies.csv', usecols=rt_cols)


# ==========================================
# 2. ERSTE EXPLORATION (Explorative Datenanalyse)
# ==========================================

print("--- IMDb Daten ---")
print(df_imdb.head())
print("\nFehlende Werte IMDb:")
print(df_imdb.isnull().sum())

print("\n--- Rotten Tomatoes Daten ---")
print(df_rt.head())
print("\nFehlende Werte Rotten Tomatoes:")
print(df_rt.isnull().sum())

print("\nDatentypen prüfen:")
print("IMDb:\n", df_imdb.dtypes)
print("\nRotten Tomatoes:\n", df_rt.dtypes)

print("--- IMDb Daten (Erste 3 Zeilen) ---")
print(df_imdb.head(3))
print("\nAnzahl Zeilen IMDB:", len(df_imdb))

print("\n--- Rotten Tomatoes Daten (Erste 3 Zeilen) ---")
print(df_rt.head(3))
print("\nAnzahl Zeilen Rotten Tomatoes:", len(df_rt))

# ==========================================
# 3. DATENBEREINIGUNG (Data Cleaning)
# ==========================================

print("\n--- Starte Datenbereinigung ---")

# 1. IMDb-Bereinigung:
# 'Released_Year' ist vom Typ String, da es teilweise falsche Werte (z.B. 'PG') enthält.
# Wir wandeln alles in numerische Werte (NaN bei Fehlern) und geben das Jahr als Integer aus.
df_imdb['Released_Year'] = pd.to_numeric(df_imdb['Released_Year'], errors='coerce')
df_imdb = df_imdb.dropna(subset=['Released_Year']) 
df_imdb['Released_Year'] = df_imdb['Released_Year'].astype(int)

# 2. Rotten Tomatoes-Bereinigung:
# Ratings ohne Wert können wir nicht für den Vergleich verwenden
df_rt = df_rt.dropna(subset=['tomatometer_rating'])

# 'original_release_date' in ein Jahr umwandeln (datetime conversion -> dt.year)
df_rt['Released_Year_RT'] = pd.to_datetime(df_rt['original_release_date'], errors='coerce').dt.year
# Entfernen der originalen Datumsspalte und Zeilen ohne Jahr
df_rt = df_rt.drop(columns=['original_release_date']).dropna(subset=['Released_Year_RT'])
df_rt['Released_Year_RT'] = df_rt['Released_Year_RT'].astype(int)

# Info nach der Bereinigung
print("\nIMDb nach Bereinigung:\n", df_imdb.info())
print("\nRotten Tomatoes nach Bereinigung:\n", df_rt.info())

# ==========================================
# 4. DATENTRANSFORMATION (Data Integration / Feature Engineering)
# ==========================================

print("\n--- Starte Datentransformation (Zusammenführen) ---")

# Vorbereitung: Umwandlung der Filmtitel in Kleinbuchstaben (Normalisierung)
# Dies stellt sicher, dass "The Godfather" auf "the godfather" gematched wird
df_imdb['title_norm'] = df_imdb['Series_Title'].str.lower().str.strip()
df_rt['title_norm'] = df_rt['movie_title'].str.lower().str.strip()

# Verknüpfung (Merge) der Datensätze über den normalisierten Titel (Inner Join)
df_merged = pd.merge(df_imdb, df_rt, on='title_norm', how='inner')

# Um Falschzuordnungen zu vermeiden (gleicher Titel, anderer Film),
# prüfen wir, ob das Erscheinungsjahr (zwischen imdb und RT) maximal 2 Jahre voneinander abweicht.
jahr_differenz_ok = abs(df_merged['Released_Year'] - df_merged['Released_Year_RT']) <= 2
df_merged = df_merged[jahr_differenz_ok].copy()

# Feature Engineering / Transformation:
# IMDb ist eine Skala von 0-10, Rotten Tomatoes von 0-100.
# Wir multiplizieren IMDb mit 10, um sie direkt zu vergleichen.
df_merged['IMDB_Rating_100'] = df_merged['IMDB_Rating'] * 10

# Bereinigung: Wir entfernen temporäre Spalten, die wir für den Vergleich nicht mehr brauchen
df_merged = df_merged.drop(columns=['title_norm', 'Released_Year_RT', 'movie_title'])

print(f"\nErfolgreich verbundene Datensätze: {len(df_merged)}")
print("\nEin Blick auf den neuen Datensatz:\n", df_merged.head())
# ==========================================
# 5. QUALITÄTSPRÜFUNG & VISUALISIERUNG
# ==========================================

print('\n--- Qualitätsprüfung ---')
# Wir prüfen statistische Kennzahlen, um Sinnhaftigkeit zu verifizieren
print(df_merged[['IMDB_Rating_100', 'tomatometer_rating']].describe())

print('\n--- Erstelle Visualisierungen ---')
sns.set_theme(style='whitegrid')

# Plot 1: Scatterplot (Korrelation)
plt.figure(figsize=(10, 6))
# Scatterplot zeichnen
sns.scatterplot(data=df_merged, x='IMDB_Rating_100', y='tomatometer_rating', alpha=0.6, color='blue', s=60)
# Diagonale Orientierungslinie (x=y) für den perfekten Match einzeichnen
plt.plot([0, 100], [0, 100], color='red', linestyle='--', linewidth=2, label='Perfekte Übereinstimmung')
plt.title('Vergleich: IMDb Publikum vs. Rotten Tomatoes Kritiker', fontsize=16, pad=15)
plt.xlabel('IMDb Rating (skaliert auf 100)', fontsize=13)
plt.ylabel('Rotten Tomatoes Rating', fontsize=13)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.xlim(50, 100)
plt.ylim(0, 105)
plt.legend(fontsize=11, loc='lower right')
plt.savefig('rating_comparison_scatter.png', dpi=300, bbox_inches='tight')
plt.close()

# Plot 2: Boxplot (Verteilung und Outlier) aufgehübscht mit Stripplot
plt.figure(figsize=(9, 6))
df_melted = df_merged[['IMDB_Rating_100', 'tomatometer_rating']].melt(var_name='Plattform', value_name='Rating')

# Ein eleganter Boxplot im Hintergrund (ohne fette, hässliche Standard-Outlier)
sns.boxplot(data=df_melted, x='Plattform', y='Rating', color='white', width=0.4, showfliers=False)

# Ein Stripplot darüber gelegt, um die tatsächliche Dichte und jeden Ausreißer als halbtransparenten Punkt (Jitter) zu zeigen
sns.stripplot(data=df_melted, x='Plattform', y='Rating', hue='Plattform', legend=False, palette='Set2', alpha=0.5, jitter=True, size=5, zorder=1)

plt.title('Rating-Verteilung: Boxplot inkl. Datendichte und Einzel-Ausreißern', fontsize=14)
plt.ylabel('Bewertungsscore (0-100)', fontsize=12)
plt.xlabel('')
plt.xticks([0, 1], ['IMDb (Publikum)', 'Rotten Tomatoes (Kritiker)'], fontsize=12)
plt.savefig('rating_distribution_boxplot.png', dpi=300, bbox_inches='tight')
plt.close()

print('Visualisierungen wurden als PNG-Dateien im Ordner gespeichert.')

# Plot 4: Epochen-Analyse / Regressions-Plot über die Jahre
# Fragestellung: Werden Kritiker über die Jahre strenger im Vergleich zum Publikum?
plt.figure(figsize=(12, 6))
sns.regplot(data=df_merged, x='Released_Year', y='Rating_Diff',
            scatter_kws={'alpha':0.4, 'color':'teal', 's':40},
            line_kws={'color':'red', 'linewidth':3})
plt.axhline(0, color='black', linestyle='--', linewidth=1.5)
plt.title('Die \"Zynismus-Lücke\": Entwicklung der Meinungsverschiedenheit über Zeit', fontsize=16, pad=15)
plt.xlabel('Veröffentlichungsjahr', fontsize=13)
plt.ylabel('Differenz (Kritiker - Publikum)', fontsize=13)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

# Lesbare Text-Boxen (damit die Datenpunkte den Text nicht überschreiben)
props = dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.8, edgecolor='gray')
plt.text(1930, -35, 'Publikum liebt es mehr\nals Kritiker (Negative Differenz)', color='black', fontsize=12, bbox=props)
plt.text(1930, 15, 'Kritiker lieben es mehr\nals Publikum (Positive Differenz)', color='black', fontsize=12, bbox=props)

plt.savefig('rating_timeline_regression.png', dpi=300, bbox_inches='tight')
plt.close()

# Plot 5: Der \"Magic Quadrant\" der Filmindustrie
imdb_median = df_merged['IMDB_Rating_100'].median()
rt_median = df_merged['tomatometer_rating'].median()

plt.figure(figsize=(12, 9))
sns.scatterplot(data=df_merged, x='IMDB_Rating_100', y='tomatometer_rating', 
                alpha=0.6, color='Slateblue', s=80, edgecolor='black', linewidth=0.5)

# Quadranten-Linien bei den Medianen deutlich hervorheben
plt.axvline(x=imdb_median, color='black', linestyle='--', alpha=0.7, linewidth=1.5)
plt.axhline(y=rt_median, color='black', linestyle='--', alpha=0.7, linewidth=1.5)

# Quadranten benennen (mit leichten Offsets zu den Rändern) inkl. Text-Boxen für perfekte Lesbarkeit
props_quadrant = dict(boxstyle='round,pad=0.6', facecolor='white', alpha=0.9, edgecolor='lightgray')

plt.text(imdb_median + 0.3, rt_median + 5, 'Universelle Meisterwerke\n(Beide lieben es)', 
         fontsize=13, color='darkgreen', weight='bold', bbox=props_quadrant)
         
plt.text(76, rt_median + 5, 'Kritiker-Lieblinge\n(Der \"Snob-Effekt\")', 
         fontsize=13, color='darkorange', weight='bold', bbox=props_quadrant)
         
plt.text(imdb_median + 0.3, 30, 'Popcorn-Kino / Kultfilme\n(Massenpublikum favorisiert es)', 
         fontsize=13, color='darkblue', weight='bold', bbox=props_quadrant)
         
plt.text(76, 30, 'Kontroverses Nischen-Kino\n(Beide werten tief)', 
         fontsize=13, color='dimgrey', weight='bold', bbox=props_quadrant)

plt.title('Der Magic Quadrant der Filmbewertungen', fontsize=18, pad=20, weight='bold')
plt.xlabel(f'IMDb Rating (Median {imdb_median})', fontsize=14)
plt.ylabel(f'Rotten Tomatoes (Median {rt_median})', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlim(75.5, 93.5)
plt.ylim(20, 105)

plt.savefig('magic_quadrant_analysis.png', dpi=300, bbox_inches='tight')
plt.close()

print('Erweiterte Analysen wurden als \"rating_timeline_regression.png\" und \"magic_quadrant_analysis.png\" gespeichert.')
