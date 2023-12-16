from items._space import Space
from items.enums import Rarity, Size


class EpicMediumSpace(Space):

    def __init__(self, id: int):
        super().__init__(id)
        self._title = "Epic Medium Space"
        self._rarity = Rarity.EPIC
        self._size = Size.MEDIUM
        self._priority = 5
        self._total_doors = 3
        self._composition = []