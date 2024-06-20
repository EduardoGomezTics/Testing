import matplotlib.pyplot as plt

def plot_poligono():
    # Datos corregidos (longitudes iguales)
    sabores = ["Cola", "Cola light", "Limón", "Manzana", "Naranaja", "Toronja"]
    frecuencias = [30, 20, 13.33, 10, 10, 16.67]

    # Crear gráfico de polígono de frecuencias de barras
    plt.figure(figsize=(10, 6))  # Tamaño opcional del gráfico
    plt.plot(sabores, frecuencias, marker='o', linestyle='-', color='b', markersize=8)
    plt.fill_between(sabores, frecuencias, color='skyblue', alpha=0.3)
    plt.title('Polígono de Frecuencias')
    plt.xlabel('Sabores')
    plt.ylabel('Frecuencia relativa')
    plt.xticks(rotation=45)  # Rotar etiquetas del eje x para mejor legibilidad
    plt.grid(True)
    plt.show()

