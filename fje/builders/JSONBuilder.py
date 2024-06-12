from builders.Builder import Builder
from components.Container import Container
from components.Leaf import Leaf

class JSONBuilder(Builder):
    def build(self, data):
        if isinstance(data, dict):
            parent = Container("root")
            for key, value in data.items():
                child = self.build(value)
                child.name = key
                parent.add(child)
            return parent
        elif data is not None:
            return Leaf("value", data)
        return Leaf("null")
