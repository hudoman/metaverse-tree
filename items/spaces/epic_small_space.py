from items._space import Space
from items.enums import Rarity, Size


class EpicSmallSpace(Space):

    def __init__(self, id: int):
        super().__init__(id)
        self._title = "Epic Small Space"
        self._rarity = Rarity.EPIC
        self._size = Size.SMALL
        self._priority = 4
        self._total_doors = 2
        self._composition = []