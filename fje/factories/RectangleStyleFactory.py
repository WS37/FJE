from factories.Factory import Factory
from styles.RectangleStyle import RectangleStyle

# 矩形风格工厂
class RectangleStyleFactory(Factory):
    def create_style():
        return RectangleStyle()
