from items._space import Space
from items.enums import Rarity, Size

class MythicMediumSpace(Space):

    def __init__(self, id: int):
        super().__init__(id)
        self._title = "Mythic Medium Space"
        self._rarity = Rarity.MYTHIC
        self._size = Size.MEDIUM
        self._priority = 11
        self._total_doors = 3
        self._composition = []