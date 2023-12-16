from items._space import Space
from items.enums import Rarity, Size

class LegendaryMediumSpace(Space):

    def __init__(self, id: int):
        super().__init__(id)
        self._title = "Legendary Medium Space"
        self._rarity = Rarity.LEGENDARY
        self._size = Size.MEDIUM
        self._priority = 8
        self._total_doors = 3
        self._composition = []