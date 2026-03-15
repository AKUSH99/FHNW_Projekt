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

# Plot 1: Scatterplot (Korrelation) - Verbessert mit Outlier-Markierungen
plt.figure(figsize=(11, 7))

# Berechne die absolute Differenz für jeden Punkt, um Outlier (Differenz > 20) zu markieren
df_merged['Abweichung'] = abs(df_merged['IMDB_Rating_100'] - df_merged['tomatometer_rating'])
df_merged['Ist_Outlier'] = df_merged['Abweichung'] > 20

# Scatterplot zeichnen (Farbgebung & Größe nach Outlier-Status)
sns.scatterplot(
    data=df_merged, x='IMDB_Rating_100', y='tomatometer_rating', 
    hue='Ist_Outlier', palette={False: '#3498db', True: '#e74c3c'},
    alpha=0.8, s=60, legend=False
)

# Die extremsten Ausreißer namentlich im Plot markieren (Studentischer Bonus)
outliers = df_merged.nlargest(4, 'Abweichung')
for _, row in outliers.iterrows():
    plt.text(row['IMDB_Rating_100'] + 0.5, row['tomatometer_rating'] - 1.5,
             row['Series_Title'], fontsize=9, color='darkred', weight='bold')

# Diagonale Orientierungslinie (x=y) für den perfekten Match einzeichnen
plt.plot([0, 100], [0, 100], color='black', linestyle='--', linewidth=1.5, label='Perfekte Übereinstimmung')

plt.title('Vergleich: Publikum vs. Kritiker (inkl. Markierung extremer Ausreißer)', fontsize=14, pad=15)
plt.xlabel('IMDb Rating (Publikum, skaliert auf 100)')
plt.ylabel('Rotten Tomatoes Rating (Kritiker)')
plt.xlim(70, 95) # Maßstab besser auf die tatsächliche IMDb-Verteilung legen
plt.ylim(10, 105)

# Moderne Legende einfügen
from matplotlib.lines import Line2D
custom_lines = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#3498db', markersize=8, label='Normale Diskrepanz'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#e74c3c', markersize=8, label='Extremer Ausreißer (>20 PKT)'),
    Line2D([0], [0], color='black', linestyle='--', lw=1.5, label='Perfekte Übereinstimmung')
]
plt.legend(handles=custom_lines, loc='lower right')

plt.tight_layout()
plt.savefig('rating_comparison_scatter.png', dpi=300)
plt.close()

# Plot 2: Boxplot (Verteilung und Outlier)
plt.figure(figsize=(8, 5))
df_melted = df_merged[['IMDB_Rating_100', 'tomatometer_rating']].melt(var_name='Plattform', value_name='Rating')
sns.boxplot(data=df_melted, x='Plattform', y='Rating', hue='Plattform', legend=False, palette='Set2')
plt.title('Rating-Verteilung der beiden Plattformen')
plt.savefig('rating_distribution_boxplot.png')
plt.close()

print('Visualisierungen wurden als PNG-Dateien im Ordner gespeichert.')

# ==========================================
# 6. ERWEITERTE ANALYSE (Genres & Diskrepanz)
# ==========================================

print('\n--- Erweiterte Segmentierung (Streitfälle & Genres) ---')

# Wir berechnen die absolute Rating-Differenz, um die grössten Diskrepanzen zu finden
df_merged['Rating_Diff'] = df_merged['tomatometer_rating'] - df_merged['IMDB_Rating_100']

# Top 5 Filme, die Kritiker viel besser fanden als das Publikum
print('\nKritiker-Lieblinge (Die RT viel besser bewertet als IMDb):')
print(df_merged.nlargest(5, 'Rating_Diff')[['Series_Title', 'IMDB_Rating_100', 'tomatometer_rating', 'Rating_Diff']])

# Top 5 Filme, die das Publikum viel besser fand als Kritiker (Negative Differenz)
print('\nPublikums-Lieblinge (Die IMDb viel besser bewertet als RT):')
print(df_merged.nsmallest(5, 'Rating_Diff')[['Series_Title', 'IMDB_Rating_100', 'tomatometer_rating', 'Rating_Diff']])

# Kleine Genre-Analyse (Wir nehmen nur das Hauptgenre, meist das erste in der Komma-Liste)
df_merged['Main_Genre'] = df_merged['Genre'].apply(lambda x: x.split(',')[0].strip())

print('\nDurchschnittliche Differenz pro Hauptgenre (Top 10 Genres nach Häufigkeit):')
top_genres = df_merged['Main_Genre'].value_counts().head(10).index
genre_diffs = df_merged[df_merged['Main_Genre'].isin(top_genres)].groupby('Main_Genre')['Rating_Diff'].mean().sort_values()
print(genre_diffs)

# ==========================================
# 7. WISSENSCHAFTLICHE SIGNIFIKANZ & ADVANCED PLOTTING
# ==========================================
from scipy import stats

print('\n--- Statistische Signifikanzprüfung (Hypothesentest) ---')
# Wir führen einen gepaarten t-Test durch, da es sich um dieselben Filme (verbundene Stichproben) handelt.
# Nullhypothese: Es gibt keinen systematischen Unterschied zwischen IMDb und RT.
t_stat, p_val = stats.ttest_rel(df_merged['IMDB_Rating_100'], df_merged['tomatometer_rating'])

print(f'T-Statistik: {t_stat:.2f}')
print(f'P-Wert: {p_val:.2e}')

if p_val < 0.05:
    print('Ergebnis: Die Nullhypothese wird abgelehnt. Der Unterschied in der Bewertung ist STATISTISCH SIGNIFIKANT und kein Zufall!')
else:
    print('Ergebnis: Die Nullhypothese bleibt bestehen. Die Unterschiede könnten Zufall sein.')

# Plot 3: Kernel Density Estimate (KDE) - Eine sehr akademische Form der Verteilungsdarstellung
plt.figure(figsize=(9, 5))
sns.kdeplot(data=df_merged, x='IMDB_Rating_100', fill=True, label='IMDb (Publikum)', color='blue', alpha=0.5)
sns.kdeplot(data=df_merged, x='tomatometer_rating', fill=True, label='Rotten Tomatoes (Kritiker)', color='green', alpha=0.3)
plt.title('Dichteverteilung (KDE) der Ratings: Publikum vs. Kritiker')
plt.xlabel('Rating (0-100)')
plt.ylabel('Dichte')
plt.legend()
plt.savefig('rating_density_kde.png')
plt.close()

print('Erweiterter KDE-Plot wurde als rating_density_kde.png gespeichert.')
