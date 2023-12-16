from items._space import Space
from items.enums import Rarity, Size

class ExaltedLargeSpace(Space):

    def __init__(self, id: int):
        super().__init__(id)
        self._title = "Exalted Large Space"
        self._rarity = Rarity.EXALTED
        self._size = Size.LARGE
        self._priority = 15
        self._total_doors = 6
        self._composition = []