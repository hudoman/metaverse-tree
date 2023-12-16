from items._space import Space
from items.enums import Rarity, Size

class ExaltedSmallSpace(Space):

    def __init__(self, id: int):
        super().__init__(id)
        self._title = "Exalted Small Space"
        self._rarity = Rarity.EXALTED
        self._size = Size.SMALL
        self._priority = 13
        self._total_doors = 3
        self._composition = []