from styles.Style import Style

# 树形风格
class TreeStyle(Style):
    def render_container(self, container, icon_family, prefix):
        result = f"{prefix}├─ {icon_family.Container()} {container.name}\n"
        for i, child in enumerate(container.children):
            if i == len(container.children) - 1:
                result += child.display(self, icon_family, prefix + "│   ")
            else:
                result += child.display(self, icon_family, prefix + "│   ")
        return result

    def render_leaf(self, leaf, icon_family, prefix):
        return f"{prefix}└─ {icon_family.Leaf()} {leaf.name}: {leaf.value}\n"
