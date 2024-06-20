import matplotlib.pyplot as plt

def plot_pie():
    datos = [30, 20, 13.33, 10, 10, 16.67]
    marcas_texto = ["Cola", "Cola light", "Limón", "Manzana", "Naranaja", "Toronja"]
    separaciones = [0, 0, 0, 0, 0, 0]

    plt.figure(figsize=(8, 8))  # Opcional: tamaño del gráfico
    plt.pie(datos, 
            explode=separaciones,
            counterclock=False,
            startangle=90, 
            autopct="%0.1f%%",
            pctdistance=0.8, 
            colors=["#37CA64", "#FF99F3", "#37C5CA", "#E74E50", "#FC8C29", "#DEE74E"],
            labels=marcas_texto)
    plt.title("Distribución de Sabores", fontsize=20)  # Opcional: título del gráfico
    plt.show()



