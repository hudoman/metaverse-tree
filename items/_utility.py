from abc import ABC
from typing import List
from .enums import Specialization, Bonus, Rarity, Color, Type, Category

class Utility(ABC):
    """
    The base Utility Item Component class declares common attributes and methods for composition.
    """
    _id: int
    _title: str
    _category: Category
    _rarity: Rarity
    _rarity_color: str
    _type: Type
    _color: Color
    _color_hex: List[str]
    _specializations: List[Specialization]
    _bonuses: List[Bonus]
    _parent: "Space"

    def __init__(self, id: int, rarity: Rarity):
        self._id = id
        self._rarity = rarity
        self._rarity_color = rarity_color_map[self._rarity]

    def __repr__(self):
        return f"{self._id}-{self._category}_{self._rarity}_{self._type}_{self._color}"

    def get_string_key(self) -> str:
        return f"{self._id}-{self._category.value}_{self._type.value}_{self._color.value}_{self._rarity.value}"

    def get_string_repr(self) -> str:
        return f"{self._category.value}_{self._type.value}_{self._color.value}_{self._rarity.value}"
    
    def set_parent(self, parent: "Space"):
        self._parent = parent

    def get_parent(self) -> "Space":
        return self._parent
    
    def get_id(self) -> int:
        return self._id
        
    def get_category(self) -> Category:
        return self._category
    
    def get_rarity(self) -> Rarity:
        return self._rarity

    def get_type(self) -> Type:
        return self._type
    

utility_color_map = {
    Color.RED: ["#FF1700"],
    Color.BLUE: ["#15F4EE"],
    Color.GREEN: ["#06FF00"],
    Color.RAINBOW: ["#ffd32a", "#15F4EE", "#06FF00"],
    Color.RED_BLUE: ["#FF1700", "#15F4EE"],
    Color.BLUE_GREEN: ["#15F4EE", "#06FF00"],
    Color.GREEN_RED: ["#06FF00", "#FF1700"]
}

rarity_color_map = {
    Rarity.COMMON: "#eeeeee",
    Rarity.UNCOMMON: "#1cbf6a",
    Rarity.RARE: "#159cfd",
    Rarity.EPIC: "#a369ff",
    Rarity.LEGENDARY: "#e67e22",
    Rarity.MYTHIC: "#ffd32a",
    Rarity.EXALTED: "#ef5777",
    Rarity.EXOTIC: "#be2edd",
    Rarity.TRANSCENDENT: "#ea96ff",
    Rarity.UNIQUE: "#68fcf5"
}
