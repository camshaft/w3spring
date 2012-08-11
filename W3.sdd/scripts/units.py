import os

import slk
# import mdx
# import blp

assets = './../assets/'

unitData = slk.readSlk(os.path.join(assets, 'War3/Units/UnitData.slk'))
unitAbilitiesData = slk.readSlk(os.path.join(assets, 'War3/Units/UnitAbilities.slk'))
unitBalanceData = slk.readSlk(os.path.join(assets, 'War3/Units/UnitBalance.slk'))
unitWeaponData = slk.readSlk(os.path.join(assets, 'War3/Units/UnitWeapons.slk'))

class UnitDef(object):
    """Holds a object that describes a unit"""

    """This is simply the name of the unit as it appears to the player."""
    name = None

    """This is the tooltip description of the unit seen by the player. It defaults to the name of the unit."""
    description = None

    """The filename of the image to be used as the build picture, assumes Unitpics/ directory"""
    buildPic = None

    """The filename of the 3D model file for this unit, assumes Objects3D/ directory."""
    objectName = None

    """The filename of the animation script file for this unit, assumes Scripts/ directory. Default assumes .cob file but LUS should be preferred."""
    script = None

    """The base 'hitpoints' the unit will have."""
    maxDamage = None

    """How much health the unit will regain every second."""
    autoHeal = None

    """How much health the unit will regain every second whilst it is idle."""
    idleAutoHeal = None

    """The time in frames taken until a unit is considered to be idle."""
    idleTime = None

    """The amount of metal resource the unit costs to build. Cannot be below 1.0."""
    buildCostMetal = None

    """The amount of energy resource the unit costs to build."""
    buildCostEnergy = None

    """
    The time taken to build the unit, in conjunction with the workerTime of the constructor.
    Effectively, Time to build = unit buildTime / constructor workerTime. Defaults to 0.0 but cannot actually be below 1.0.
    """
    buildTime = None

    """The mass of the unit, used in weapon impulse calculations. Cannot be less than 1.0."""
    mass = None

    """Can the unit be reclaimed by a builder?"""
    reclaimable = None

    """Can a unit be stolen by a builder using the capture command?"""
    capturable = None

    """Can the unit be repaired by a builder?"""
    repairable = None

    """The maximum cumulative speed at which this unit can be repaired."""
    maxRepairSpeed = None

    """The name of the radar icon type this unit should use"""
    iconType = None

    """The name of the feature this unit should leave behind as a wreck when it dies"""
    corpse = None

    """The name of the weapon this unit should explode as when it is killed"""
    explodeAs = None

    """The name of the weapon this unit should explode as when it self destructs"""
    selfDestructAs = None

id = 'hpea'
peasantData = None
peasantAData = None
peasantBData = None
peasantWData = None

for index, unit in unitData.items():
    if unit['unitID'] == id:
        peasantData = unit
for index, unit in unitAbilitiesData.items():
    if unit['unitAbilID'] == id:
        peasantAData = unit
for index, unit in unitBalanceData.items():
    if unit['unitBalanceID'] == id:
        peasantBData = unit
for index, unit in unitWeaponData.items():
    if unit['unitWeapID'] == id:
        peasantWData = unit


print peasantData
print peasantAData
print peasantBData
print peasantWData
