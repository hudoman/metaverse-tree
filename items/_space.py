from abc import ABC
from typing import List, Union
from .enums import Category, Rarity, Size
from ._utility import Utility

class Space(ABC):
    """
    The base SPACE Item Component class declares common operations for objects of a composition.
    """
    _id: int
    _title: str
    _category: Category
    _rarity: Rarity
    _size: Size
    _priority: int
    _total_doors: int
    _parent: "Space"
    _composition: List[Union["Space", Utility]]

    def __init__(self, id: int):
        self._id = id
        self._category = Category.SPACE

    def __repr__(self):
        return f"{self._id}-{self._rarity}_{self._size}_{self._category}"
    
    def add(self, component: Union["Space", Utility]) -> None:
        if not self.has_available_door():
            raise AssertionError("Not enough doors!")
        self._composition.append(component)

    def get_id(self) -> int:
        return self._id

    def get_rarity(self) -> Rarity:
        return self._rarity

    def get_category(self) -> Category:
        return self._category
          
    def set_parent(self, parent: "Space"):
        self._parent = parent

    def get_parent(self) -> "Space":
        return self._parent
    
    def get_composition(self) -> List[Union["Space", Utility]]:
        return self._composition
    
    def get_total_doors(self) -> int:
        return self._total_doors

    def available_doors(self) -> int:
        return self._total_doors - len(self._composition)
    
    def has_available_door(self) -> bool:
        available = self.available_doors()
        if available == 0:
            return False
        else:
            return True