from typing import Optional

from pydantic import BaseModel, Field


class FortStringObject(BaseModel):
    namespace: str
    key: str
    source_string: str = Field(alias='sourceString')


class FortItemText(BaseModel):
    value: FortStringObject
    text: str = Field(alias='finalText')
    history_type: str = Field(alias='historyType')
    

class DisplayAssetPath(BaseModel):
    path: str = Field(alias='assetPath')
    sub_path: str = Field(alias='subPath')


class DisplayName(FortItemText):
    ...


class Description(FortItemText):
    ...


class ShortDescription(FortItemText):
    ...


class FortBaseCosmetic(BaseModel):
    item_type: str = Field(alias='exportType')
    name: DisplayName = Field(alias='DisplayName')
    description: Description = Field(alias='Description')
    short_description: ShortDescription = Field(alias='ShortDescription')
    rarity: Optional[str] = Field(default='EFortRarity::Common', alias='Rarity')
    series: Optional[str] = Field(alias='Series')
    preview_image: Optional[DisplayAssetPath] = Field(alias='LargePreviewImage')
    display_asset: Optional[DisplayAssetPath] = Field(alias='DisplayAssetPath')

    @property
    def image(self):
        return self.preview_image or self.display_asset
