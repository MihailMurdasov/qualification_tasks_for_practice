from graphviz import Digraph


def plot_tree_graphviz(root):
    def add_edges(node, dot=None):
        if dot is None:
            dot = Digraph()

        if node is not None:
            dot.node(str(node.key))
            if node.left:
                dot.node(str(node.left.key))
                dot.edge(str(node.key), str(node.left.key))
                add_edges(node.left, dot)
            if node.right:
                dot.node(str(node.right.key))
                dot.edge(str(node.key), str(node.right.key))
                add_edges(node.right, dot)
        return dot

    dot = add_edges(root)
    return dot

def visualize_avl(root, filename="avl_tree"):
    """
        Выполняет визуализацию АВЛ-дерева.
    """
    dot = plot_tree_graphviz(root)
    dot.render(filename, format="png", cleanup=True)
