import matplotlib.pyplot as plt

def plot_ojiva():
    datos = marcas_clase = [1, 2, 3, 4, 5, 6]  # Datos del eje x 
    frecuencias = [0.3, 0.5, 0.63, 0.73, 0.83, 1]  # Frecuencias acumuladas
    marcas_texto = ["Cola", "Cola light", "Limón", "Manzana", "Naranaja", "Toronja"]  # Etiquetas para el eje x 

    # Ajustes necesarios para trazar el polígono
    datos_x = [0] + marcas_clase 
    datos_y = [0] + frecuencias  

    plt.figure(figsize=(12, 6))  # Ancho, alto de la figura 

    plt.plot(datos_x, datos_y, 
             linewidth=5, color="b", linestyle=":", 
             marker="v", markersize=15, markerfacecolor="y", markeredgecolor="r")

    plt.xticks(marcas_clase, marcas_texto, fontsize=15, rotation=45)  # Colocar texto sobre el eje x 
    plt.xlabel("Marcas de clase", fontsize=20)  # Etiqueta del eje x
    plt.ylabel("Frecuencias", fontsize=20)  # Etiqueta del eje y 
    plt.title("Ojiva", fontsize=25)  # Título del gráfico

    plt.grid()  # Se activa la cuadrícula sobre el gráfico 
    plt.show()  # Se muestra el gráfico

