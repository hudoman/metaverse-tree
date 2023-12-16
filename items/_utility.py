from abc import ABC
from typing import List, Union

from .enums import Specialization, Bonus, Rarity, Color, Type, Category

class Utility(ABC):
    """
    The base Utility Item Component class declares common attributes and methods for composition.
    """
    _id: int
    _title: str
    _category: Category
    _rarity: Rarity
    _type: Type
    _color: Color
    _specializations: List[Specialization]
    _bonuses: List[Bonus]
    _parent: "Space"

    def __init__(self, id: int, rarity: Rarity):
        self._id = id
        self._rarity = rarity

    def __repr__(self):
        return f"{self._id}-{self._rarity}_{self._type}_{self._color}_{self._category}"
    
    def set_parent(self, parent: "Space"):
        self._parent = parent

    def get_parent(self) -> "Space":
        return self._parent
    
    def get_id(self) -> int:
        return self._id

    def get_category(self) -> Category:
        return self._category