import c4d
from c4d import documents, plugins, storage
# Try to load an object.

def main():
    file_to_load = "Y:\\My Drive\\Dyne - LLL\\Xmas Card 2019\\04_3D\\01_C4D\\02_ScnElements\\EP00_ACT00\\TrickyXmas_Materials_Arbol_v14 (Mats Only).c4d"

    # Import without dialogs
    c4d.documents.MergeDocument(doc, file_to_load, c4d.SCENEFILTER_OBJECTS|c4d.SCENEFILTER_MATERIALS , None)

    c4d.EventAdd()
    
if __name__=='__main__':
    main()