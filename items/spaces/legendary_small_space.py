from items._space import Space
from items.enums import Rarity, Size

class LegendarySmallSpace(Space):

    def __init__(self, id: int):
        super().__init__(id)
        self._title = "Legendary Small Space"
        self._rarity = Rarity.LEGENDARY
        self._size = Size.SMALL
        self._priority = 7
        self._total_doors = 2
        self._composition = []