import pandas as pd

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