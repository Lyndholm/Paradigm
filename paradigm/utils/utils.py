from paradigm import models


def define_asset_type(export_type: str):
    match export_type:
        case 'AthenaCharacterItemDefinition':
            return models.FortCharacter
        case 'AthenaBackpackItemDefinition':
            return models.FortBackpack
        case 'AthenaPickaxeItemDefinition':
            return models.FortPickaxe
        case 'AthenaGliderItemDefinition':
            return models.FortGlider
        case 'AthenaSkyDiveContrailItemDefinition':
            return models.FortSkyDiveContrail
        case 'AthenaDanceItemDefinition':
            return models.FortDance
        case 'AthenaItemWrapDefinition':
            return models.FortItemWrap
        case 'AthenaPetCarrierItemDefinition':
            return models.FortPetCarrier
        case 'AthenaEmojiItemDefinition':
            return models.FortEmoji
        case 'FortVariantTokenType':
            return models.FortVariantStyle
        case 'AthenaSprayItemDefinition':
            return models.FortSpray
        case 'AthenaMusicPackItemDefinition':
            return models.FortMusicPack
        case 'AthenaLoadingScreenItemDefinition':
            return models.FortLoadingScreen
        case 'FortBannerTokenType':
            return models.FortBanner
        case 'AthenaToyItemDefinition':
            return models.FortToy
        case _:
            raise TypeError(f'Undefined type: {export_type}')


def change_rarity_based_on_series(asset: models.FortBaseCosmetic) -> None:
    match asset.series:
        case 'ColumbusSeries':
            asset.rarity = 'StarWars'
        case 'CreatorCollabSeries':
            asset.rarity = 'Icon'
        case 'CUBESeries':
            asset.rarity = 'Dark'
        case 'DCUSeries':
            asset.rarity = 'DC'
        case 'FrozenSeries':
            asset.rarity = 'Frozen'
        case 'LavaSeries':
            asset.rarity = 'Lava'
        case 'MarvelSeries':
            asset.rarity = 'Marvel'
        case 'PlatformSeries':
            asset.rarity = 'GamingLegends'
        case 'ShadowSeries':
            asset.rarity = 'Shadow'
        case 'SlurpSeries':
            asset.rarity = 'Slurp'
