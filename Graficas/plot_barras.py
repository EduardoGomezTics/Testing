import matplotlib.pyplot as plt

def plot_barras():
    marcas_clase = [1, 2, 3, 4, 5, 6]
    frecuencias = [9, 6, 4, 3, 3, 5]
    marcas_texto = ["Cola", "Cola light", "Limón", "Manzana", "Naranaja", "Toronja"]

    plt.figure(figsize=(12, 6))

    plt.barh(marcas_clase, frecuencias, 
             height=0.75, edgecolor="k", 
             color=["#37CA64", "#FF99F3", "#37C5CA", "#E74E50", "#FC8C29", "#DEE74E"])

    plt.yticks(marcas_clase, marcas_texto, fontsize=15)
    plt.xlabel("Marcas de clase", fontsize=20)
    plt.ylabel("Frecuencias", fontsize=20)
    plt.title("Diagrama de barras", fontsize=25)

    plt.grid()
    plt.show()



