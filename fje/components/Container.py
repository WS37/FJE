from components.Component import Component

class Container(Component):
    def __init__(self, name, level=0):
        super().__init__(name)
        self.children = []
        self.level = level
        self.icon = None

    def add(self, component):
        self.children.append(component)
        
    def display(self, style, icon_family, prefix=''):
        self.icon = icon_family.Container
        return style.render_container(self, icon_family, prefix)