from styles.Style import Style

# 矩形风格
class RectangleStyle(Style):
    def render_container(self, container, icon_family, prefix):
        firstline = "─"*(64-len(f"{prefix}┌─ {icon_family.Container()} {container.name}")) + "┐"
        result = f"{prefix}┌─ {icon_family.Container()} {container.name} {firstline}\n"
        for child in container.children:
            result += child.display(self, icon_family, prefix + "│  ")
        lastline = "└"+"─"*(64-len(f"{prefix}")) + "┘"
        result += f"{prefix}{lastline}\n"
        return result

    def render_leaf(self, leaf, icon_family, prefix):
        leafresult = f"{prefix}├─ {icon_family.Leaf()} {leaf.name}: {leaf.value} "
        return leafresult + "─"*(64-len(leafresult)) + "│\n"
