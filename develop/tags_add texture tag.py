def addTexTag(obj, layer, mat):
    textag = c4d.TextureTag()
    textag.SetMaterial(mat)
    textag[c4d.ID_BASELIST_NAME] = mat[c4d.ID_BASELIST_NAME]
    textag[c4d.TEXTURETAG_PROJECTION] = c4d.TEXTURETAG_PROJECTION_UVW
    textag[c4d.ID_LAYER_LINK] = layer
    obj.InsertTag(textag)
    return textag