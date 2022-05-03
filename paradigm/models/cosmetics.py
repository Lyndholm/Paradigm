from typing import Optional

from pydantic import Field

from .base import FortBaseCosmetic


class FortCharacter(FortBaseCosmetic):
    definition_path: str = Field(alias='HeroDefinition')


class FortBackpack(FortBaseCosmetic):
    ...


class FortPickaxe(FortBaseCosmetic):
    ...


class FortGlider(FortBaseCosmetic):
    ...


class FortSkyDiveContrail(FortBaseCosmetic):
    ...


class FortDance(FortBaseCosmetic):
    ...


class FortItemWrap(FortBaseCosmetic):
    ...


class FortPetCarrier(FortBaseCosmetic):
    ...


class FortVariantStyle(FortBaseCosmetic):
    ...


class FortEmoji(FortBaseCosmetic):
    ...


class FortSpray(FortBaseCosmetic):
    rarity: Optional[str] = Field(default='EFortRarity::Uncommon', alias='Rarity')


class FortMusicPack(FortBaseCosmetic):
    ...


class FortLoadingScreen(FortBaseCosmetic):
    rarity: Optional[str] = Field(default='EFortRarity::Uncommon', alias='Rarity')


class FortBanner(FortBaseCosmetic):
    ...


class FortToy(FortBaseCosmetic):
    ...
