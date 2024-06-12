from components.Component import Component

class Leaf(Component):
    def __init__(self, name, value=None):
        super().__init__(name)
        self.value = value
        self.icon = None

    def display(self, style, icon_family, prefix=''):
        self.icon = icon_family.Leaf
        return style.render_leaf(self, icon_family, prefix)
