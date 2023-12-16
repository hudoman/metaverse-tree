from items._utility import Utility
from items.enums import TimeWardenBonus, TimeWardenSpecialization, Category, Rarity, Type, Color

class ATimeWarden(Utility):
    def __init__(self, id: int, rarity: Rarity):
        super().__init__(id, rarity)
        self._title = "Time Warden of Brilliance"
        self._category = Category.TIME_WARDEN
        self._type = Type.A
        self._color = Color.RED_BLUE
        self._specializations = [
            TimeWardenSpecialization.RECHARGING
        ]
        self._bonuses = [ 
            TimeWardenBonus.SPEED,
            TimeWardenBonus.EFFICIENTY
        ]

class BTimeWarden(Utility):
    def __init__(self, id: int, rarity: Rarity):
        super().__init__(id, rarity)
        self._title = "Time Warden of Prosperity"
        self._category = Category.TIME_WARDEN
        self._type = Type.B
        self._color = Color.BLUE_GREEN
        self._specializations = [
            TimeWardenSpecialization.CRAFTING
        ]
        self._bonuses = [ 
            TimeWardenBonus.LUCK,
            TimeWardenBonus.EFFICIENTY
        ]

class CTimeWarden(Utility):
    def __init__(self, id: int, rarity: Rarity):
        super().__init__(id, rarity)
        self._title = "Time Warden of Expedience"
        self._category = Category.TIME_WARDEN
        self._type = Type.C
        self._color = Color.GREEN_RED
        self._specializations = [
            TimeWardenSpecialization.RECHARGING,
            TimeWardenSpecialization.CRAFTING_50
        ]
        self._bonuses = [ 
            TimeWardenBonus.SPEED,
            TimeWardenBonus.LUCK
        ]

class DTimeWarden(Utility):
    def __init__(self, id: int, rarity: Rarity):
        super().__init__(id, rarity)
        self._title = "Time Warden of Ascendancy"
        self._category = Category.TIME_WARDEN
        self._type = Type.D
        self._color = Color.RAINBOW
        self._specializations = [
            TimeWardenSpecialization.RECHARGING,
            TimeWardenSpecialization.CRAFTING_100
        ]
        self._bonuses = [ 
            TimeWardenBonus.SPEED,
            TimeWardenBonus.EFFICIENTY,
            TimeWardenBonus.LUCK
        ]