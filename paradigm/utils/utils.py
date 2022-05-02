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
