from enum import auto
from strenum import StrEnum

class Category(StrEnum):
    SPACE = "space"
    FORGE = "forge"
    ARMORY = "armory"
    TIME_WARDEN = "time_warden"

class Size(StrEnum):
    TINY = "tiny"
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"

class Type(StrEnum):
    A = auto()
    B = auto()
    C = auto()
    D = auto()
    E = auto()
    F = auto()
    G = auto()
    H = auto()
    I = auto()
    J = auto()

class Color(StrEnum):
    RED = "red"
    BLUE = "blue"
    GREEN = "green"
    RAINBOW = "rainbow"
    RED_BLUE = "red/blue"
    BLUE_GREEN = "blue/green"
    GREEN_RED = "green/red"

class Rarity(StrEnum):
    COMMON = "common"
    UNCOMMON = "uncommon"
    RARE = "rare"
    EPIC = "epic"
    LEGENDARY = "legendary"
    MYTHIC = "mythic"
    EXALTED = "exalted"
    EXOTIC = "exotic"
    TRANSCENDENT = "transcendent"
    UNIQUE = "unique"

class Specialization(StrEnum):
    ...

class Bonus(StrEnum):
    ...

class Specialization(StrEnum):
    ...

class ForgeSpecialization(Specialization):
    TWO_HAND_AXE = "2-Hand Axe"
    TWO_HAND_SWORD = "2-Hand Sword"
    TWO_HAND_HAMMER = "2-Hand Hammer"
    ONE_HAND_WEAPONS = "1-Hand Weapons"
    STAVES = "Staves"
    DUAL_WIELD = "Dual Wield"

class ForgeBonus(Bonus):
    SPEED = "Faster Crafting & Refining"
    EFFICIENTY = "Less $TIME needed when Crafting & Refining"
    LUCK = "Extra Bonus Roll Slot"

class ArmorySpecialization(Specialization):
    GLOVES = "Gloves"
    HELMETS = "Helmets"
    SHOULDERS = "Shoulders"
    CHEST = "Chest"
    LEGS = "Legs"
    SHIELDS = "Shields"

class ArmoryBonus(Bonus):
    SPEED = "Faster Crafting & Refining"
    EFFICIENTY = "Less $TIME needed when Crafting & Refining"
    LUCK = "Extra Bonus Roll Slot"

class TimeWardenSpecialization(Specialization):
    RECHARGING = "Recharging Hourglass"
    CRAFTING = "Crafting Hourglass"
    CRAFTING_50 = "Crafting Hourglass (50%)"
    CRAFTING_100 = "Crafting Hourglass (100%)"

class TimeWardenBonus(Bonus):
    SPEED = "5% Faster Crafting & Recharging"
    EFFICIENTY = "5% Less Time Crystals Cost"
    LUCK = "1 Extra Bonus Roll Slot"
