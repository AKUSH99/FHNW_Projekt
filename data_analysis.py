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

print("--- IMDb Daten (Erste 3 Zeilen) ---")
print(df_imdb.head(3))
print("\nAnzahl Zeilen IMDB:", len(df_imdb))

print("\n--- Rotten Tomatoes Daten (Erste 3 Zeilen) ---")
print(df_rt.head(3))
print("\nAnzahl Zeilen Rotten Tomatoes:", len(df_rt))