import json
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# Define Functions for ID3 Algorithm
def entropy(labels):
    n = len(labels)
    if n == 0:
        return 0.0
    probs = labels.value_counts() / n
    return -np.sum(probs * np.log2(probs))

def information_gain(df, feature, target):
    parent_entropy = entropy(df[target])
    weighted_child = sum(
        (len(subset) / len(df)) * entropy(subset[target])
        for _, subset in df.groupby(feature)
    )
    return parent_entropy - weighted_child

def best_feature(df, features, target):
    gains = {f: information_gain(df, f, target) for f in features}
    print("Information Gains:", {k: round(v, 4) for k, v in gains.items()})
    return max(gains, key=gains.get)

def ID3(df, features, target):
    if len(df[target].unique()) == 1:
        return df[target].iloc[0]

    if not features:
        return df[target].mode()[0]

    best = best_feature(df, features, target)
    tree = {best: {}}

    for value, subset in df.groupby(best):
        tree[best][value] = ID3(
            subset,
            [f for f in features if f != best],
            target,
        )

    return tree

# Load Dataset
dir_path = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(dir_path, "barcelona_ucl_dataset.csv"))
TARGET = "Result"

# Build Decision Tree
tree = ID3(df, [col for col in df.columns if col != TARGET], TARGET)
print("Decision Tree:", json.dumps(tree, indent=2))

# Build Recursive Tree Layout
def subtree_width(node):
    if not isinstance(node, dict):
        return 1
    root = list(node.keys())[0]
    return sum(subtree_width(child) for child in node[root].values())

def add_nodes(graph, node, parent=None, edge_label="", x=0, y=0):
    if isinstance(node, dict):
        root = list(node.keys())[0]
        node_id = f"node_{len(graph.nodes())}"
        graph.add_node(node_id, label=root)
        graph.nodes[node_id]["pos"] = (x, y)
        if parent is not None:
            graph.add_edge(parent, node_id, label=edge_label)

        children = node[root]
        total_width = sum(subtree_width(child) for child in children.values())
        start_x = x - total_width / 2
        offset = start_x
        for branch, child in children.items():
            width = subtree_width(child)
            child_x = offset + width / 2
            add_nodes(graph, child, parent=node_id, edge_label=branch, x=child_x, y=y - 2)
            offset += width
        return node_id
    else:
        leaf_id = f"leaf_{len(graph.nodes())}"
        graph.add_node(leaf_id, label=node)
        graph.nodes[leaf_id]["pos"] = (x, y)
        if parent is not None:
            graph.add_edge(parent, leaf_id, label=edge_label)
        return leaf_id

def collect_positions(graph):
    return {n: data["pos"] for n, data in graph.nodes(data=True)}

# Create and visualize the tree
g = nx.DiGraph()
add_nodes(g, tree, x=0, y=0)
pos = collect_positions(g)
labels = nx.get_node_attributes(g, "label")
edge_labels = nx.get_edge_attributes(g, "label")

plt.figure(figsize=(14, 9))
nx.draw_networkx_nodes(g, pos, node_color="#5B9BD5", node_size=2800, node_shape="s")
nx.draw_networkx_labels(g, pos, labels, font_size=10, font_color="white", font_weight="bold")
nx.draw_networkx_edges(g, pos, arrows=True, arrowsize=20, edge_color="#555555", width=1.8)
for (u, v), label in edge_labels.items():
    x1, y1 = pos[u]
    x2, y2 = pos[v]
    plt.text((x1 + x2) / 2, (y1 + y2) / 2, label,
             fontsize=9, color="#333333",
             bbox=dict(boxstyle="round,pad=0.2", fc="lightyellow", ec="gray", alpha=0.8),
             ha="center", va="center")

plt.title("Decision Tree — Will Barcelona Win the UCL?", fontsize=16, fontweight="bold", pad=20)
plt.axis("off")
plt.tight_layout()
plt.savefig(os.path.join(dir_path, "barcelona_decision_tree.png"), dpi=220)
plt.close()
print("Saved tree visualization to barcelona_decision_tree.png")
