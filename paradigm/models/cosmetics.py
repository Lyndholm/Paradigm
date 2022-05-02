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


class FortEmoji(FortBaseCosmetic):
    ...


class FortSpray(FortBaseCosmetic):
    ...


class FortMusicPack(FortBaseCosmetic):
    ...


class FortLoadingScreen(FortBaseCosmetic):
    ...


class FortBanner(FortBaseCosmetic):
    ...


class FortToy(FortBaseCosmetic):
    ...
