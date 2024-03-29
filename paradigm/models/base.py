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
    name: DisplayName | None = Field(alias='DisplayName')
    description: Description | None = Field(alias='Description')
    short_description: ShortDescription | None = Field(alias='ShortDescription')
    rarity: str | None = Field(default='EFortRarity::Common', alias='Rarity')
    series: str | None = Field(alias='Series')
    fmodel_path: str | None
    gameplay_tags: list[str] | None = Field(alias='GameplayTags', default=[])
    preview_image: DisplayAssetPath | None = Field(alias='LargePreviewImage')
    display_asset: DisplayAssetPath | None = Field(alias='DisplayAssetPath')

    @property
    def image(self):
        return self.preview_image or self.display_asset

    @property
    def path(self):
        return self.fmodel_path or self.name.text.replace(' ', '')
