import os
import pydot
import networkx as nx
import matplotlib.pyplot as plt


def render_gv_to_png(gv_path: str, output_png: str = None):
    if not os.path.isfile(gv_path):
        raise FileNotFoundError(f"No existe el archivo: {gv_path}")

    if output_png is None:
        output_png = os.path.splitext(gv_path)[0] + ".png"

    graphs = pydot.graph_from_dot_file(gv_path)

    if not graphs:
        raise ValueError(f"No se pudo leer el archivo .gv: {gv_path}")

    dot_graph = graphs[0]

    G = nx.nx_pydot.from_pydot(dot_graph)

    G.remove_nodes_from(["\\n", "\n", "", None])

    if len(G.nodes) == 0:
        raise ValueError(f"El archivo no contiene nodos válidos: {gv_path}")

    # Ignora pesos de aristas para evitar error int + str
    pos = nx.spring_layout(G, seed=42, weight=None)

    plt.figure(figsize=(10, 7))

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=1800,
        font_size=10,
        arrows=G.is_directed(),
        edgecolors="black"
    )

    plt.savefig(output_png, format="png", bbox_inches="tight")
    plt.close()

    print(f"Imagen generada: {output_png}")


def render_carpeta_gv(carpeta: str):
    if not os.path.isdir(carpeta):
        raise FileNotFoundError(f"No existe la carpeta: {carpeta}")

    archivos_gv = [
        archivo for archivo in os.listdir(carpeta)
        if archivo.lower().endswith(".gv")
    ]

    if not archivos_gv:
        print("No se encontraron archivos .gv en la carpeta.")
        return

    for archivo in archivos_gv:
        ruta_gv = os.path.join(carpeta, archivo)

        try:
            render_gv_to_png(ruta_gv)
        except Exception as e:
            print(f"Error con el archivo: {archivo}")
            print(f"Detalle: {e}")
            print("-" * 50)


carpeta_gv = r"C:\Users\tono7\Downloads\Proyecto 3-20260510T234826Z-3-001\Imagenes"

render_carpeta_gv(carpeta_gv)