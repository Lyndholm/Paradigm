import utils

from bot import Paradigm


bot = Paradigm()
paths_to_parse = (
    utils.BACKPACKS_PATH,
    utils.BANNERS_PATH,
    utils.EMOJIS_PATH,
    utils.EMOTES_PATH,
    utils.GLIDERS_PATH,
    utils.ITEM_WRAPS_PATH,
    utils.LOADING_SCREENS_PATH,
    utils.MUSIC_PACKS_PATH,
    utils.OUTFITS_PATH,
    # utils.PICKAXES_PATH,
    # utils.PICKAXES_ALT_PATH,
    utils.SKYDIVING_TRAILS_PATH,
    utils.SPRAYS_PATH,
    utils.STYLES_PATH,
    utils.TOYS_PATH,
)


def main() -> None:
    assets = bot.get_added_files()

    for path in paths_to_parse:
        bot.generate_asset_icons(assets, path)


if __name__ == '__main__':
    main()
