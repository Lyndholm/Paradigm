import time
from typing import Any, Optional

import requests

import creator
import utils


class Paradigm:
    BASE = 'https://benbot.app/api/v1/'

    def __init__(self) -> None:
        self.sesion = requests.Session()
        self.logger = utils.logger.setup_logger(__class__.__name__)


    def get_added_files(self) -> Optional[dict[str, Any]]:
        r = self.sesion.get(f'{self.BASE}files/added')
        if r.status_code != 200:
            return

        return r.json()


    def get_asset_properties(self, asset: str) -> Optional[dict[str, Any]]:
        r = self.sesion.get(
            f'{self.BASE}assetProperties',
            params={
                'lang': 'ru',
                'path': asset
            }
        )
        if r.status_code != 200:
            return

        data = r.json()['export_properties'][0]
        return data


    def generate_asset_icons(self, assets_list: list, asset_path_pattern: str) -> None:
        assets = list(
            filter(
                lambda asset: asset.startswith(asset_path_pattern),
                assets_list
            )
        )
        for asset in assets:
            properties = self.get_asset_properties(asset)
            item = utils.define_asset_type(properties['exportType'])
            icon = creator.BaseIcon(item(**properties, fmodel_path=asset))
            icon.generate_icon()
            self.logger.info(f'Generated: {asset}')
            time.sleep(3) # sleep for 3 seconds, we don't want to spam the api

        utils.merge_images()
