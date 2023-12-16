
from items._utility import Utility, utility_color_map
from items._space import Space
from items.enums import ForgeBonus, ForgeSpecialization, Category, Rarity, Type, Color

class AForge(Utility):
    def __init__(self, id: int, rarity: Rarity):
        super().__init__(id, rarity)
        self._title = "Forge of Quickness"
        self._category = Category.FORGE
        self._type = Type.A
        self._color = Color.RED
        self._color_hex = utility_color_map[self._color]
        self._specializations = [
            ForgeSpecialization.TWO_HAND_AXE
        ]
        self._bonuses = [ 
            ForgeBonus.SPEED
        ]

class BForge(Utility):
    def __init__(self, id: int, rarity: Rarity):
        super().__init__(id, rarity)
        self._title = "Forge of Rapidness"
        self._category = Category.FORGE
        self._type = Type.B
        self._color = Color.RED
        self._color_hex = utility_color_map[self._color]
        self._specializations = [
            ForgeSpecialization.TWO_HAND_SWORD
        ]
        self._bonuses = [ 
            ForgeBonus.SPEED
        ]

class CForge(Utility):
    def __init__(self, id: int, rarity: Rarity):
        super().__init__(id, rarity)
        self._title = "Forge of Swiftness"
        self._category = Category.FORGE
        self._type = Type.C
        self._color = Color.RED
        self._color_hex = utility_color_map[self._color]
        self._specializations = [
            ForgeSpecialization.STAVES,
            ForgeSpecialization.DUAL_WIELD
        ]
        self._bonuses = [ 
            ForgeBonus.SPEED
        ]

class DForge(Utility):
    def __init__(self, id: int, rarity: Rarity):
        super().__init__(id, rarity)
        self._title = "Forge of Decisiveness"
        self._category = Category.FORGE
        self._type = Type.D
        self._color = Color.BLUE
        self._color_hex = utility_color_map[self._color]
        self._specializations = [
            ForgeSpecialization.TWO_HAND_HAMMER
        ]
        self._bonuses = [ 
            ForgeBonus.EFFICIENTY
        ]

class EForge(Utility):
    def __init__(self, id: int, rarity: Rarity):
        super().__init__(id, rarity)
        self._title = "Forge of Diligence"
        self._category = Category.FORGE
        self._type = Type.E
        self._color = Color.BLUE
        self._color_hex = utility_color_map[self._color]
        self._specializations = [
            ForgeSpecialization.ONE_HAND_WEAPONS
        ]
        self._bonuses = [ 
            ForgeBonus.EFFICIENTY
        ]

class FForge(Utility):
    def __init__(self, id: int, rarity: Rarity):
        super().__init__(id, rarity)
        self._title = "Forge of Acuity"
        self._category = Category.FORGE
        self._type = Type.F
        self._color = Color.BLUE
        self._color_hex = utility_color_map[self._color]
        self._specializations = [
            ForgeSpecialization.TWO_HAND_SWORD,
            ForgeSpecialization.TWO_HAND_AXE
        ]
        self._bonuses = [ 
            ForgeBonus.EFFICIENTY
        ]

class GForge(Utility):
    def __init__(self, id: int, rarity: Rarity):
        super().__init__(id, rarity)
        self._title = "Forge of Chance"
        self._category = Category.FORGE
        self._type = Type.G
        self._color = Color.GREEN
        self._color_hex = utility_color_map[self._color]
        self._specializations = [
            ForgeSpecialization.STAVES
        ]
        self._bonuses = [ 
            ForgeBonus.LUCK
        ]

class HForge(Utility):
    def __init__(self, id: int, rarity: Rarity):
        super().__init__(id, rarity)
        self._title = "Forge of Luck"
        self._category = Category.FORGE
        self._type = Type.H
        self._color = Color.GREEN
        self._color_hex = utility_color_map[self._color]
        self._specializations = [
            ForgeSpecialization.DUAL_WIELD
        ]
        self._bonuses = [ 
            ForgeBonus.LUCK
        ]

class IForge(Utility):
    def __init__(self, id: int, rarity: Rarity):
        super().__init__(id, rarity)
        self._title = "Forge of Fortune"
        self._category = Category.FORGE
        self._type = Type.I
        self._color = Color.GREEN
        self._color_hex = utility_color_map[self._color]
        self._specializations = [
            ForgeSpecialization.TWO_HAND_HAMMER,
            ForgeSpecialization.ONE_HAND_WEAPONS
        ]
        self._bonuses = [ 
            ForgeBonus.LUCK
        ]

# class JForge(Utility):
#     def __init__(self, id: int, rarity: Rarity):
#         super().__init__(id, rarity)
#         self._title = "Forge of Triumph"
#         self._category = Category.FORGE
#         self._type = Type.J
#         self._color = Color.RAINBOW
#         self._color_hex = utility_color_map[self._color]
#         self._specializations = [
#             ForgeSpecialization.TWO_HAND_SWORD,
#             ForgeSpecialization.TWO_HAND_AXE,
#             ForgeSpecialization.TWO_HAND_HAMMER,
#             ForgeSpecialization.ONE_HAND_WEAPONS,
#             ForgeSpecialization.STAVES,
#             ForgeSpecialization.DUAL_WIELD
#         ]
#         self._bonuses = [ 
#             ForgeBonus.SPEED,
#             ForgeBonus.EFFICIENTY,
#             ForgeBonus.LUCK,
            
#         ]