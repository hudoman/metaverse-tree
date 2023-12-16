from items._space import Space
from items.enums import Rarity, Size

class ExaltedMediumSpace(Space):

    def __init__(self, id: int):
        super().__init__(id)
        self._title = "Exalted Medium Space"
        self._rarity = Rarity.EXALTED
        self._size = Size.MEDIUM
        self._priority = 14
        self._total_doors = 4
        self._composition = []