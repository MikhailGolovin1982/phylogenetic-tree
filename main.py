import json
import networkx as nx
import matplotlib.pyplot as plt

# Функция для чтения данных из файла JSON
def read_tree_structure(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

# Функция для построения графа
def build_graph(tree_structure):
    G = nx.DiGraph()
    for child, parents in tree_structure.items():
        for parent in parents:
            G.add_edge(parent, child)
    return G

# Функция для визуализации графа и сохранения в файл
def visualize_and_save_graph(G, output_path="phylogenetic_tree.png"):
    G_reversed = G.reverse()  # Инвертируем граф для направления "родители → потомки"
    plt.figure(figsize=(12, 8))
    pos = nx.nx_agraph.graphviz_layout(G_reversed, prog="dot")  # Древообразная раскладка
    nx.draw(
        G_reversed,
        pos,
        with_labels=True,
        node_size=2000,
        font_size=10,
        node_color="lightgreen",
        font_color="black",
        arrows=True,
        arrowstyle="->",
        arrowsize=20,
    )
    plt.title("Филогенетическое дерево (родители → потомки)", fontsize=16)
    plt.savefig(output_path, format="png", dpi=300, bbox_inches="tight")
    plt.close()  # Закрываем plt, чтобы освободить память
    print(f"Изображение сохранено в {output_path}")

# Основной скрипт
if __name__ == "__main__":
    # Укажите путь к файлу JSON с данными дерева
    file_path = "tree_structure.json"  # Замените на путь к вашему файлу
    tree_structure = read_tree_structure(file_path)
    
    # Построение графа
    G = build_graph(tree_structure)
    
    # Сохранение графа в файл
    visualize_and_save_graph(G, "phylogenetic_tree.png")
