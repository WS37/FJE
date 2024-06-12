import argparse
import json
import importlib
from builders.JSONBuilder import JSONBuilder


class FJE:
    def __init__(self, style_factory, icon_factory):
        self.style_factory = style_factory
        self.icon_factory = icon_factory

    def show(self, data):
        builder = JSONBuilder()
        root = builder.build(data)
        style = self.style_factory.create_style()
        icon = self.icon_factory.create_icon()
        print(root.display(style, icon))

# 加载 JSON 文件
def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)
    
def get_module(module_path):
    module_name, class_name = module_path.rsplit('.', 1)
    module = importlib.import_module(module_name)
    return getattr(module, class_name)

config = load_json("config.json")
parser = argparse.ArgumentParser(description="Funny JSON Explorer")
parser.add_argument('-f', '--file', type=str, required=True, help='Path to the JSON file')
parser.add_argument('-s', '--style', choices=list(config["styles"].keys()), default='tree', help="Style to display JSON")
parser.add_argument('-i', '--icon_family', choices=list(config["icon_families"].keys()), default='card', help="Icon family to use")
args = parser.parse_args()

def main():
    data = load_json(args.file)
    example = FJE(get_module(config["styles"][args.style]), get_module(config["icon_families"][args.icon_family]))
    example.show(data)

if __name__ == '__main__':
    main()
