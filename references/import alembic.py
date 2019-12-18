import c4d
from c4d import documents, plugins, storage
# Try to load an object.

def main():
    file_to_load = "Y:\\My Drive\\Dyne - LLL\\Xmas Card 2019\\08_Delivery\\06_Transfer\\Simon_Maya Export Tutorial_duende.abc"

    #file_to_load = "Y:\\My Drive\\Dyne - LLL\\Xmas Card 2019\\04_3D\\03_Maya\\Character_Idle\\Tree\\TrickyXmas_Tree_idle_v02.abc"

    # Import without dialogs
    c4d.documents.MergeDocument(doc, file_to_load, c4d.SCENEFILTER_OBJECTS|c4d.SCENEFILTER_MATERIALS , None)

    c4d.EventAdd()
    
if __name__=='__main__':
    main()