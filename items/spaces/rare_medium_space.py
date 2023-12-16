from items._space import Space
from items.enums import Rarity, Size

class RareMediumSpace(Space):
    
    def __init__(self, id: int):
        super().__init__(id)
        self._title = "Rare Medium Space"
        self._rarity = Rarity.RARE
        self._size = Size.MEDIUM
        self._priority = 2
        self._total_doors = 3
        self._composition = []