from icon_families.Icon_family import Icon_family

class Card(Icon_family):
    def Container(self):
        return "♦"  # 方块
    
    def Leaf(self):
        return "♠"  # 黑桃