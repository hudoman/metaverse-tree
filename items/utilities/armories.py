
from items._utility import Utility
from items.enums import ArmoryBonus, ArmorySpecialization, Category, Rarity, Type, Color

class AArmory(Utility):
    def __init__(self, id: int, rarity: Rarity):
        super().__init__(id, rarity)
        self._title = "Armory of Quickness"
        self._category = Category.ARMORY
        self._type = Type.A
        self._color = Color.RED
        self._specializations = [
            ArmorySpecialization.GLOVES
        ]
        self._bonuses = [ 
            ArmoryBonus.SPEED
        ]

class BArmory(Utility):
    def __init__(self, id: int, rarity: Rarity):
        super().__init__(id, rarity)
        self._title = "Armory of Rapidness"
        self._category = Category.ARMORY
        self._type = Type.B
        self._color = Color.RED
        self._specializations = [
            ArmorySpecialization.HELMETS
        ]
        self._bonuses = [ 
            ArmoryBonus.SPEED
        ]

class CArmory(Utility):
    def __init__(self, id: int, rarity: Rarity):
        super().__init__(id, rarity)
        self._title = "Armory of Swiftness"
        self._category = Category.ARMORY
        self._type = Type.C
        self._color = Color.RED
        self._specializations = [
            ArmorySpecialization.LEGS,
            ArmorySpecialization.SHIELDS
        ]
        self._bonuses = [ 
            ArmoryBonus.SPEED
        ]

class DArmory(Utility):
    def __init__(self, id: int, rarity: Rarity):
        super().__init__(id, rarity)
        self._title = "Armory of Decisiveness"
        self._category = Category.ARMORY
        self._type = Type.D
        self._color = Color.BLUE
        self._specializations = [
            ArmorySpecialization.SHOULDERS
        ]
        self._bonuses = [ 
            ArmoryBonus.EFFICIENTY
        ]

class EArmory(Utility):
    def __init__(self, id: int, rarity: Rarity):
        super().__init__(id, rarity)
        self._title = "Armory of Diligence"
        self._category = Category.ARMORY
        self._type = Type.E
        self._color = Color.BLUE
        self._specializations = [
            ArmorySpecialization.CHEST
        ]
        self._bonuses = [ 
            ArmoryBonus.EFFICIENTY
        ]

class FArmory(Utility):
    def __init__(self, id: int, rarity: Rarity):
        super().__init__(id, rarity)
        self._title = "Armory of Acuity"
        self._category = Category.ARMORY
        self._type = Type.F
        self._color = Color.BLUE
        self._specializations = [
            ArmorySpecialization.GLOVES,
            ArmorySpecialization.HELMETS
        ]
        self._bonuses = [ 
            ArmoryBonus.EFFICIENTY
        ]

class GArmory(Utility):
    def __init__(self, id: int, rarity: Rarity):
        super().__init__(id, rarity)
        self._title = "Armory of Chance"
        self._category = Category.ARMORY
        self._type = Type.G
        self._color = Color.GREEN
        self._specializations = [
            ArmorySpecialization.LEGS
        ]
        self._bonuses = [ 
            ArmoryBonus.LUCK
        ]

class HArmory(Utility):
    def __init__(self, id: int, rarity: Rarity):
        super().__init__(id, rarity)
        self._title = "Armory of Luck"
        self._category = Category.ARMORY
        self._type = Type.H
        self._color = Color.GREEN
        self._specializations = [
            ArmorySpecialization.SHIELDS
        ]
        self._bonuses = [ 
            ArmoryBonus.LUCK
        ]

class IArmory(Utility):
    def __init__(self, id: int, rarity: Rarity):
        super().__init__(id, rarity)
        self._title = "Armory of Fortune"
        self._category = Category.ARMORY
        self._type = Type.I
        self._color = Color.GREEN
        self._specializations = [
            ArmorySpecialization.SHOULDERS,
            ArmorySpecialization.CHEST
        ]
        self._bonuses = [ 
            ArmoryBonus.LUCK
        ]

class JArmory(Utility):
    def __init__(self, id: int, rarity: Rarity):
        super().__init__(id, rarity)
        self._title = "Armory of Triumph"
        self._category = Category.ARMORY
        self._type = Type.J
        self._color = Color.RAINBOW
        self._specializations = [
            ArmorySpecialization.GLOVES,
            ArmorySpecialization.HELMETS,
            ArmorySpecialization.SHOULDERS,
            ArmorySpecialization.CHEST,
            ArmorySpecialization.LEGS,
            ArmorySpecialization.SHIELDS
        ]    

        self._bonuses = [ 
            ArmoryBonus.SPEED,
            ArmoryBonus.EFFICIENTY,
            ArmoryBonus.LUCK,
            
        ]