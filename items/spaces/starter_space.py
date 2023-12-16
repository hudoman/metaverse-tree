from items._space import Space
from items.enums import Rarity, Size


class StarterSpace(Space):

    def __init__(self, id: int):
        super().__init__(id)
        self._title = "Starter Space"
        self._rarity = Rarity.COMMON
        self._size = Size.TINY
        self._priority = 0
        self._total_doors = 1
        self._composition = []