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