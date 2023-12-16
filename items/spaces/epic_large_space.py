from items._space import Space
from items.enums import Rarity, Size


class EpicLargeSpace(Space):

    def __init__(self, id: int):
        super().__init__(id)
        self._title = "Epic Large Space"
        self._rarity = Rarity.EPIC
        self._size = Size.LARGE
        self._priority = 6
        self._total_doors = 5
        self._composition = []