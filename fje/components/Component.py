class Component:
    def __init__(self, name):
        self.name = name

    def add(self, component):
        raise NotImplementedError

    def display(self, style, icon_family, prefix=''):
        raise NotImplementedError
