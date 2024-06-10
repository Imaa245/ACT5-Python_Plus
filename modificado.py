import pandas as pd

# Ruta del archivo
file_route = "area_protegida.csv"

# Lectura del archivo
df = pd.read_csv(file_route, encoding='utf-8')

# Conteo de ocurrencias en la columna 7
conteos = df.iloc[:, 6].value_counts()

# Obtención de las 5 ocurrencias más altas
top_rating = conteos.head(5).items()

# Función para imprimir un informe
def print_report(title, *args):
    print(f"{title.capitalize():-^40}")
    for elem in args:
        print(f"{elem[0]}: {elem[1]}")

# Impresión del informe con las 3 ocurrencias más altas
top_rating_list = list(top_rating)
print_report("Super listado", top_rating_list[0], top_rating_list[1], top_rating_list[2])

print(df.shape)