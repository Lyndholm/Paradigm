from typing import Optional

from pydantic import Field

from .base import FortBaseCosmetic


class FortCharacter(FortBaseCosmetic):
    definition_path: str = Field(alias='HeroDefinition')
    sorting_priority = 0


class FortBackpack(FortBaseCosmetic):
    sorting_priority = 1


class FortPickaxe(FortBaseCosmetic):
    sorting_priority = 2


class FortGlider(FortBaseCosmetic):
    sorting_priority = 3


class FortSkyDiveContrail(FortBaseCosmetic):
    sorting_priority = 7


class FortDance(FortBaseCosmetic):
    sorting_priority = 4


class FortItemWrap(FortBaseCosmetic):
    sorting_priority = 5


class FortPetCarrier(FortBaseCosmetic):
    sorting_priority = 12


class FortVariantStyle(FortBaseCosmetic):
    sorting_priority = 99


class FortEmoji(FortBaseCosmetic):
    sorting_priority = 10


class FortSpray(FortBaseCosmetic):
    rarity: Optional[str] = Field(default='EFortRarity::Uncommon', alias='Rarity')
    sorting_priority = 9


class FortMusicPack(FortBaseCosmetic):
    sorting_priority = 6


class FortLoadingScreen(FortBaseCosmetic):
    rarity: Optional[str] = Field(default='EFortRarity::Uncommon', alias='Rarity')
    sorting_priority = 8


class FortBanner(FortBaseCosmetic):
    sorting_priority = 11


class FortToy(FortBaseCosmetic):
    sorting_priority = 13
