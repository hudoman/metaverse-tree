from items._space import Space
from items.enums import Rarity, Size

class RareSmallSpace(Space):

    def __init__(self, id: int):
        super().__init__(id)
        self._title = "Rare Small Space"
        self._rarity = Rarity.RARE
        self._size = Size.SMALL
        self._priority = 1
        self._total_doors = 2
        self._composition = []