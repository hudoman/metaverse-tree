from items._space import Space
from items.enums import Rarity, Size

class RareLargeSpace(Space):
    
    def __init__(self, id: int):
        super().__init__(id)
        self._title = "Rare Large Space"
        self._rarity = Rarity.RARE
        self._size = Size.LARGE
        self._priority = 3
        self._total_doors = 5
        self._composition = []