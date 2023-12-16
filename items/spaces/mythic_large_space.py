from items._space import Space
from items.enums import Rarity, Size

class MythicLargeSpace(Space):

    def __init__(self, id: int):
        super().__init__(id)
        self._title = "Mythic Large Space"
        self._rarity = Rarity.MYTHIC
        self._size = Size.LARGE
        self._priority = 12
        self._total_doors = 5
        self._composition = []