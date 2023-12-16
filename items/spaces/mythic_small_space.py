from items._space import Space
from items.enums import Rarity, Size

class MythicSmallSpace(Space):

    def __init__(self, id: int):
        super().__init__(id)
        self._title = "Mythic Small Space"
        self._rarity = Rarity.MYTHIC
        self._size = Size.SMALL
        self._priority = 10
        self._total_doors = 2
        self._composition = []