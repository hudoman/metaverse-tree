from items._space import Space
from items.enums import Rarity, Size

class LegendaryLargeSpace(Space):

    def __init__(self, id: int):
        super().__init__(id)
        self._title = "Legendary Large Space"
        self._rarity = Rarity.LEGENDARY
        self._size = Size.LARGE
        self._priority = 9
        self._total_doors = 5
        self._composition = []