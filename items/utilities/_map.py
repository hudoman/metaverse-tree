from typing import Dict, List
from .forges import *
from .armories import *
from .time_wardens import *
from items.enums import (
    ForgeSpecialization, 
    ForgeBonus,
    ArmorySpecialization,
    ArmoryBonus,
    TimeWardenSpecialization,
    TimeWardenBonus,
    Color
)

forge_by_bonus = {
    ForgeBonus.SPEED.value : [
        AForge,
        BForge,
        CForge,
        # JForge
    ],
    ForgeBonus.EFFICIENTY.value : [
        DForge,
        EForge,
        FForge,
        # JForge
    ],
    ForgeBonus.LUCK.value : [
        GForge,
        HForge,
        IForge,
        # JForge
    ],
}

armory_by_bonus = {
    ArmoryBonus.SPEED.value : [
        AArmory,
        BArmory,
        CArmory,
        # JArmory
    ],
    ArmoryBonus.EFFICIENTY.value : [
        DArmory,
        EArmory,
        FArmory,
        # JArmory
    ],
    ArmoryBonus.LUCK.value : [
        GArmory,
        HArmory,
        IArmory,
        # JArmory
    ],
}

time_warden_by_bonus = {
    TimeWardenBonus.SPEED.value : [
        ATimeWarden,
        CTimeWarden,
        # DTimeWarden
    ],
    TimeWardenBonus.EFFICIENTY.value : [
        ATimeWarden,
        BTimeWarden,
        # DTimeWarden
    ],
    TimeWardenBonus.LUCK.value : [
        BTimeWarden,
        CTimeWarden,
        # DTimeWarden
    ],
}

forge_by_specialization = {
    ForgeSpecialization.TWO_HAND_AXE.value : [
        AForge,
        FForge,
        # JForge
    ],
    ForgeSpecialization.TWO_HAND_HAMMER.value : [
        DForge,
        IForge,
        # JForge
    ],
    ForgeSpecialization.TWO_HAND_SWORD.value : [
        BForge,
        FForge,
        # JForge
    ],
    ForgeSpecialization.ONE_HAND_WEAPONS.value : [
        EForge,
        IForge,
        # JForge
    ],
    ForgeSpecialization.DUAL_WIELD.value : [
        CForge,
        HForge,
        # JForge
    ],
    ForgeSpecialization.STAVES.value : [
        CForge,
        GForge,
        # JForge
    ],
}

armory_by_specialization = {
    ArmorySpecialization.GLOVES.value : [
        AArmory,
        FArmory,
        # JArmory
    ],
    ArmorySpecialization.HELMETS.value : [
        BArmory,
        FArmory,
        # JArmory  
    ],
    ArmorySpecialization.SHOULDERS.value : [
        DArmory,
        IArmory,
        # JArmory
    ],
    ArmorySpecialization.CHEST.value : [
        EArmory,
        IArmory,
        # JArmory
    ],
    ArmorySpecialization.LEGS.value : [
        CArmory,
        GArmory,
        # JArmory
    ],
    ArmorySpecialization.SHIELDS.value : [
        CArmory,
        HArmory,
        # JArmory
    ],
}

time_warden_by_specialization = {
    TimeWardenSpecialization.RECHARGING.value : [
        ATimeWarden,
        CTimeWarden,
        # DTimeWarden
    ],
    TimeWardenSpecialization.CRAFTING.value : [
        BTimeWarden
    ],
    TimeWardenSpecialization.CRAFTING_50.value : [
        CTimeWarden
    ],
    TimeWardenSpecialization.CRAFTING_100.value : [
        # DTimeWarden
    ],
}

forge_by_specialization_keyed = {
    "2-hand-axe" : [
        AForge,
        FForge,
        # JForge
    ],
    "2-hand-hammer" : [
        DForge,
        IForge,
        # JForge
    ],
    "2-hand-sword" : [
        BForge,
        FForge,
        # JForge
    ],
    "1-hand-weapons" : [
        EForge,
        IForge,
        # JForge
    ],
    "dual-wield" : [
        CForge,
        HForge,
        # JForge
    ],
    "staves" : [
        CForge,
        GForge,
        # JForge
    ],
}

armory_by_specialization_keyed = {
    "gloves" : [
        AArmory,
        FArmory,
        # JArmory
    ],
    "helmets" : [
        BArmory,
        FArmory,
        # JArmory  
    ],
    "shoulders" : [
        DArmory,
        IArmory,
        # JArmory
    ],
    "chest" : [
        EArmory,
        IArmory,
        # JArmory
    ],
    "legs" : [
        CArmory,
        GArmory,
        # JArmory
    ],
    "shields" : [
        CArmory,
        HArmory,
        # JArmory
    ],
}

time_warden_by_specialization_keyed = {
    "recharging" : [
        ATimeWarden,
        CTimeWarden,
        # DTimeWarden
    ],
    "crafting" : [
        BTimeWarden,
        # DTimeWarden
    ]
}

utilities_by_category: Dict[Category, List[Utility]] = {
    Category.ARMORY : [
        AArmory,
        BArmory,
        CArmory,
        DArmory,
        EArmory,
        FArmory,
        GArmory,
        HArmory,
        IArmory,
        # JArmory
    ],
    Category.FORGE : [
        AForge,
        BForge,
        CForge,
        DForge,
        EForge,
        FForge,
        GForge,
        HForge,
        IForge,
        # JForge,
    ],
    Category.TIME_WARDEN : [
        ATimeWarden,
        BTimeWarden,
        CTimeWarden,
        # DTimeWarden
    ],
}


all_utilities: List[Utility] = [
    AArmory,
    BArmory,
    CArmory,
    DArmory,
    EArmory,
    FArmory,
    GArmory,
    HArmory,
    IArmory,
    # JArmory,
    AForge,
    BForge,
    CForge,
    DForge,
    EForge,
    FForge,
    GForge,
    HForge,
    IForge,
    # JForge,
    ATimeWarden,
    BTimeWarden,
    CTimeWarden,
    # DTimeWarden
]