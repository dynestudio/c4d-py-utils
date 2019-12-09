import c4d

def main():
    bd = doc.GetActiveBaseDraw()
    camera = bd.GetSceneCamera(doc)

    camerat[c4d.CAMERA_FOCUS] = 55

    c4d.EventAdd()

main()