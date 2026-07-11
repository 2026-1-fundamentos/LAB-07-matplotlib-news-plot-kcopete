"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    import os
    import pandas as pd
    import matplotlib.pyplot as plt

    # Leer los datos
    df = pd.read_csv("files/input/news.csv", index_col=0)

    # Crear carpeta de salida
    os.makedirs("files/plots", exist_ok=True)

    # Crear figura
    plt.figure(figsize=(8, 6))

    # Graficar
    plt.plot(df.index, df["Television"], color="dimgray", linewidth=2, marker="o")
    plt.plot(df.index, df["Newspaper"], color="gray", linewidth=2, marker="o")
    plt.plot(df.index, df["Radio"], color="lightgray", linewidth=2, marker="o")
    plt.plot(df.index, df["Internet"], color="tab:blue", linewidth=3, marker="o")

    # Título
    plt.title("How people get their news")

    # Etiquetas de los ejes
    plt.xlabel("Year")
    plt.ylabel("Percentage")

    # Leyenda
    plt.legend()

    # Guardar la imagen
    plt.savefig("files/plots/news.png")

    plt.close()
    
